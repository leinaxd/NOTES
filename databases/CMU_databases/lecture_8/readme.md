# Lecture 8: INDEX CONCURRENCY CONTROL

## INTROUDCTION
Today's lecture is going to be about index concurrency control.

Questions from last class.
1. Non-prefix lookups in multi-attribute B+Trees

2. Efficiently merging B+Trees
   -  Approach 1. Offline, blocks all operations until done merging
   -  Approach 2. Eager, access both merge, move batches eagerly
   -  Approach 3. Background, copy+merge in background; apply missed updates
   -  APproach 4. Lazy, designate one as many and other as secondary. if leaf in main not yet updated, merge correspondly key range from secondary.


### SHARE NOTHING SYSTEMS
Observation.
- We have assumed that all the data structure are single threaded
- But we need to allow multiple threads to safely access our dataa structures to take advantage of additional CPU cores and hide disk I/O stalls.

The following don't do this: (they are primarily in-memory systems)
- REDIS
- VOLTDB
- H-STORE


If you are in memory then you don't need to worry about disk I/O stalls.
- so you can get rid of concurrency control.
- and the way that we'll avoid any kind of concurrency errors is by particioning the dbms into disjoint sub-ranges.
for example, 
- keys you could split up into the k keys from 'a' to 'd', 'e' to 'j'
- partitioning the range in this way, let each partition operate in a single thread.


### CONCURRENCY CONTROL
A concurrency control protocol is the method that the DBMS uses to ensure 'correct' results to concurrent operations on a shared object.

A protocol's correctness criteria can vary,
- **LOGICAL CORRECTNESS**, can a thread see the data that it is supposed to see?
   - if i write a 5, then i want to read it, i have to be able to read my own writes.
- **PHYSICAL CORRECTNESS**, is the internal representation of object sound?
   - we have to protect the internal representation
   - the pointers, tuple layout
 

### TODAY's AGENDA
- LATCHES OVERVIEW
- HASH TABLE LATCHING
- B+TREE LATCHING
- LEAF NODE SCANS

## LOCKS VS LATCHES
**LOCKS**, 
- Protects the database's logical contents from other's transactions
- Held for transactions duration
- Need to be able to rollback changes (undo chamges in case of error)

It protects, tuples, pages, tables or abstractions.
- they are not low level physical detail
Ensures consistent and atomic transaction.


**LATCHES**,
- Protects the critical sections of the DBMS's internal data structurea from other's threads
- Held for operation duration (as short as possible)
- Do not need to be able to rollback changes. (if some occur happened, nothing has to be done)

BOOK:
- Modern B+TREE Techniques.

In latches we have no notion of deadlocks.
- also latches are embeded in the data structure
  
![](1.jpg)

We will review this at lecture 16

### LATCH MODES
**READ MODE**, 
- Multiple Threads can read the same object at the same time
- A thread  can acquire the read latch if  another thread has it in  read mode.

**WRITE MODE**,
- Only one thread can access the object
- A thread cannot acquire a write latch if another thread has it in any mode.

![](2.jpg)


### LATCH IMPLEMENTATION
- BLOCKING OS MUTEX
- TEST-AND-SET-SPIN LATCH
- READER-WRITER LATCHES

#### BLOCKING OS MUTEX
- Simple to use
- Non scalable (about 25ns per lock/unlock invocaton)
- example std::mutex

Example 
- In linux, its a typedef which is something called a futex.
   - Fast User space Mutex.
 
![](3.jpg)

It has 2 latches inside.
- Fast user space Spin Latch
- This heavyweight blocking OS Latch

Imagine we have 2 concurrent threads, they both want to acquire this locks.
- they first are going to go to the **fast user space latch**
- let's say that the left one wins
  
![](4.jpg)

- the other one, is going to  have to block and wait to the heavy weight latch.

![](5.jpg)

One the first thread is done, is going to unlock and woke up the next thread.

#### TEST-AND-SET-SPIN LATCH (TAS)
- Very Efficient (sinlge instruction to latch/unlatch)
- non-scalable, non cache friendly, not OS-friendly
- example std::atomic<T>

Entirely in the user space code. doesn't rely into the OS

Issues.
- cache coherence, multiple threads that need to cross memory boundaries in order to  acquire the same latch.
- you can also run into this contention problem, if you have lots of threads that all trying to have the same latch,
  what you end up doing is just looping forever.

Every time i call latch.test_and_set(),
- if i don't get the latch, then i drop into this loop

There's no visibility about what  instructions i'm actually executing.
- is just me looping for something.
- the os doesn't know what i'm doing
  
![](6.jpg)


#### READER-WRITTER LATCHES
- Allows for  concurrent readers
- Must manage read/write queues to avoid starvation
- can be implemented on top of spin latches

Think about the first 2 approaches as primitives, and this is like a higher level construct.

Imagine a separate read-write latch inside our big read-write latch.
- we have two counters
   - The number of threads that have successfully acquired (either read or write latch)
   - and the number of threads that are waiting (either read or write latch)

Our first thread show up, and wants to acquire a read latch.
- we are going give it out,
- and increment our count of active read latches by 1

![](7.jpg)

Another thread shows up, also wants a read latch.
- there's no problem here, we are going to give it out
- increment the count by one
  
![](8.jpg)

Let's say another thread shows up, but this want a write latch.
- we are going to block that thread, as we have stuff being read
- increment the waiting queue by 1.

![](9.jpg)

Imagine another reader shows up.
- it requires a read latch.

what do we do?
- wait the writter to finish?
- Prioritize the reader stack?
- Timestamp criterion,
- we don't care the order, as we are consistent.

To prevent starvation, we are putting the reader to wait.

![](10.jpg)


## HASH TABLE LATCHING
Easy to support concurrent access due to the limited ways threads access the data structure.
- all threads move in the same direction and only access a single page/slot at a time
- Deadlocks are not possible

To resize the table, take a global write latch on the entire table 
- e.g. in the header page

Two approaches, 
- PAGE LATCHING
  SLOT LATCHES

If i have more latches that i need to store,
- in slot latches they're fine grainer than the page level.
- i'm trading storage for more fine-grained access


Two threads might need to access different slots, 
- but only one will be able to proceed
- if there's a lock on the page.
  
### PAGE LATCHES
- Each page has its own reader-writter latch that protects its entire contents
- Threads acquire either a read or write latch before they access a page.



### SLOT LATCHES
- Each slot has its own latch
- Can use a single-mode latch to reduce meta-data and computational overhead.


