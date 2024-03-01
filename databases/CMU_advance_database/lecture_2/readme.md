# Lecture 2

## Background
Hardware was much different when the original DBMSs were designed
- Uniprocessor CPU
- Ram was severely limited
- The database had to be stored on disk
- Disk were even slower than they are now.

You always want to run databases on new hardware and get the best performance you can get out of it


But the high level of ideas from back then is almost the same, but limitations are not the same.

- Back then, machines didn't have lot of sockets

**Nowadays**, DRAM capacities are large enough that most databases can fit in memory.
- Structured datasets are smaller
  - Well defined schema
- Unstructured or Semi-structured data sets are larger

We need to understand, why we can't always use a traditional disk oriented DBMS with a large Cache to get best performance.

Many databases are not as large as you think they actually are.


There's no magic in structured data to do vectorized query execution in video data. You have to convert your video data in structured data and run your queries on it.

If my database can mostly fit on main memory, can i take a traditional disk or a database system.
Can we run that on a machine with a large enough v-ram and set a buffer cached size to be big enough 
so that everything is going to fit in memory. And the spoiler is going to be no. We need to understand why.

Today's agenda is 
- Disk oriented DBMS
- In-memory DBMS
- Concurrency Control Bottlenecks


## Disk-Oriented DBMS
The primary storage location of the database is on non-volatile storage (HDD, SSD)

The database is organized as a set of fixed-length **pages** (aka blocks)

The system uses an in-memory **Buffer Pool** to cache pages fetched from the disk
- its **job** is to manage the **movement** of those pages back and forth between **disk** and **memory**


### Buffer Pool
When a Query access a **page**, the DBMS checks to see if that page **is** already in **memory**.
- If it's not, then the DBMS must **retrieve** it from the disk and copy it into a **frame** in its buffer pool.
- If there are **no free frames**, then find a page to evict (free).
  (LRU algorithm, clock any policy to evict frames)
- If the page being **evicted** is **dirty**, then the DBMS must **write** it back to the disk. (more slow stuff to do)

Once the page is in memory, the DBMS translates any on disk addresses to their in memory addresses.

### High level disk oriented data organization
Suppose we are doing a query, that's going to look up an index.
- it wants to find a record
- The record is inside a page
- and we have to fetch it from disk.
  
![](1.jpg)

To simplify our discussion, lets say the index is not backed by buffer pool pages. It's just sitting in memory.
- in most systems that's actually not true.
- The index pages themselves would be backed up by the powerful manager.
- So we have to go check to see whether those pages are in memory as well. and do this entire process.

So the first thing to do is to look up into the index to find our record
- What the index will give us is the **page id** and the **slot number**
- And then we can use that page ID to look on a **page table** and find the location of the page we are looking for.

![](2.jpg)

- So let's say we are looking for **page 1**, and then we would **not** find the entry in our page table or we'd see an entry that says oh it's not in memeory it's **on disk**. And here is where to go find it on disk
- In order to bring the page on **memory**, we have to go **pick** an **existing page** to vicked.
- So we **latch** this page table, to make sure nobody else is trying to bring it in the same time we are.

![](3.jpg)

- Then we have to pick one of those pages to evict, so lets evict **page 2**

![](4.jpg)

- But Page 2 is dirty, so we gotta write it out to **disk**, and flush it.
- And when it's done, then we can use the free frame to copy in **page 1**

![](5.jpg)

- At this point now we update our **page table** to be able to say, hey if you look in for page 1, here's the frame.
- And once that has been done, we can **release** our **latches**.

![](6.jpg)

So what's the **problem** with this.
Let's give our database a **lot of memory**, and now everything is going to **fit** into memory.
- well we still going to the **entire process** to go look up the page
- and try to do a translation of like the **record id** to its memory location, every single time we access a tuple.
- and we have to take **latches** and protect things, because we don't want us to be accessed in the page 
- while have **another** to try **evict** that page.

If everything fits into memory all this latching is a wasting of work.
- and then running all those metrics of **eviction policy** to updating all internal metrics about how
pages are going to be access that's a waste of work too.

This sort of answers his strawman question at the beginning that, "can't we just give it a lot of memory and that be enough for getting about the same performance as we would get in an in-memory system.
- The answer is no, because we're doing this extra work just to access a single page.
 
- Every tuple access goes through the buffer pool manager regardless of whether that data will always be in memory.
- Always translate a tuple's record id to its memory location
- Worker thread must **pin** pages that it needs to make sure that they are not swapped to disk



This is going to cascade to other issues as well
### Concurrency Control
The systems assumes that a transaction could **stall** at any time whenever it tries to **access data** that is **not in memory**.
- Execute **other txns** at the same time so that if one txn **stalls** then others **keep running**
- set **locks** to provide **ACID** guarantees for txns
- **Locks** are stored in a **separate data** structure to avoid being swapped to disk.

- Concurrency protocol that could be setting locks in our own records or objects in the database, to make sure we provide the asset guarantees that you want for transactions.
- If now a transaction modifies a page,then that page gets written on the disk before that transaction commits,
  before some other transaction evict that page. Then we got to make sure that we keep track of all the section
  information, and if we crash and come back, the uncommited transactions changes don't persist.

So in a disk or any system, if it's using lockinga, it's going to maintain this locking information in separate data structure. In a memory hash table, in the lock manager to avoid those the lock information getting swapped out to disks that way i don't have to determine whether i can ever hold the lock on a tuple to go got the disk and figure out, go fetch that lock information, everything is going to be in memory.

## Logging and Recovery
Other problems with in-memory systems is Logging and recovering.

Most DBMS use **Steal + No-Force** Buffer pool policies, so all modifications have to be flushed to disk to the WAL before
a txn can commit.

Each log entry contains the before and after image of record modified

Lots of work to keep track of LSNs all throughout the DBMS

Now in memory systems we don't have dirty pages anymore, so maybe we don't want to use the exact same protocol.
And maybe our log entry don't need to store the exact same information as we have in disk oriented systems

we don't need to keep track of the logs sequence numbers, again maintaining the undo information, again dirty pages didn't get rid of disks, everything fits in memory.

## Disk Oriented DBMS overhead
There was an MIT study back in 2008, where they took an old tv database system, and they've instrumented
so they can measure the number of instructions that the data system was spending in differents parts of 
the current querry execution while you are running TPC-C.

The idea is to break down the system into different components and just **measure** how much **time** we are spending in each of them.

- Okay,this is for a database that everything **fits into memory**, nothing is flushed to disk
- What is the **cost** of **accessing** data that's in **memory**?

![](7.jpg)

- The First overhead is in the buffer manager this is about 34% of the CPU instructions spent doing updates
or looks ups into the page table. Keep track of all the metadata you have for the eviction policy.

- Then 14% of the time is spent doing latching, for this could be by the data structure such as the page table with the lock manager ran anytime, the low level constructor we need protect.

- 16% of the time is spent locking, so this particular system it was called 'sure' and uses **two-phases locking**, so this is the overhead of updating the lock information for transactions while they run.

- 12% of the instructions are spent in the log manager, so this is not the cost of running out the disk, this is the cost of preparing the log records that we're going to write down.

- 16% are spent doing a comparison of keys, doing traversals in the B+ tree, but this is sort unavoidable,
if i'm trying to find the record that i want through the D+ tree, this is the cost of comparing keys.

- 7% so this is going to leave us with a paltry 7% of the CPU instructions actually doing what they would call
real work like executing the logic for transactions, getting back to the data and then performing the commit operation.

So this is showing that if you take a disk system and you give it all memory that it wants you are not going to get potentialy the best performance, because everything could still have pain the penalty for all this internal architecture that assumes the data in not on disk, and there's all this protection mechanisms for that assumption.

## In-memory DBMSs
Assume that the primary Storage location of the database is **permanently in memory**
Early ideas  proposed in 1980s but it is now feasible because DRAM prices are low and capacities are high

First comercial In-memory DBMS were relased in 1990
- Times Ten
- Data Blitz
- Altibase

### Data Organization
An In-Memory DBMS does not need to **store** the database in slotted pages but it will still organize tuples
in **blocks** or **pages**.
- direct **memory pointers** vs **record ids**
- **Fixed length** vs **variable length** data pools
- Use **checksums** to detect software errors from trashing the database

The OS organize in memory too.

If everything lays in memory there's a thread that anybody can wrongly write the database data.

### High Level Example
- We have a query that access a tuple
- then go through an index to look it up.

Now our index, instead of returning back a **record id** or **page ID** in an offset,
We're now gonna get a **Block id** and an offset.
- And the Block id could either be the **direct memory** address of a fixed length block
- or it could be an additional mechanism that allows us to look it up and see you've convert that block id
  to a memory location
  
![](8.jpg)

So the primary search locations database again is in memory, or every tuple in memory, 
- But we're going to **organize** them in this **fixed length records**

It doesn't matter what we are assuming a row or a column.

When we want to do a lookup to find the tuple within the offset of that block we just do some simple memory arithmetic to take the size of the tuple, multiplied by our offset and then tell us where to be jump in memory to that block and regret it.


![](9.jpg)

Now to handle **variable length data**, this is going to be much different than what we would do in a disk
based system.
- Instead of storing the data in line of the fixed length data block 
- for most of the time restore a pointer to some other memory location
- in a very length data pool
- where that's a direct access to the data that corresponds to this attribute within this tuple

The idea is that we can guarantee that all tuples, and the fixed length data blocks are fixed length
and then for everything that's variable length we shove into the very lengthy data block.

Again this is different from the slotted page design you would see in a disk coordinate system, 
because in there, we're trying reduce the number of disk reads, so therefore we try to pack in all
variable length data for a tuple within the tuple itself all the fixed length data.
Doesn't always happen and if its spillover to another page, we can do that but most of the time.

In this world, **in memory system** were actually want to **store** the **variable length data**, **separately**.
- So that way we can do deterministic lookups, to find memory addresses for tuples

### Indexes
How we're actually store indexes? which data structure?
- Spoiler is B+ trees is going to be the best datastructure to use
- Originally B+ trees were designed for disk based databases, they're still really good for in memory data as well.

The other difference between indexes in that
- in a disk based system you would also write log records and write out pages for the index disk so you can
  recover them after the system restarts.
- An in-memory system, we're not actually going to record any log record to not write indexes out of the disk.
  Because, the cost of rebuilding the index after restart is going to be super low.


Specialized main-memory indexes were proposed in 1980s when cache and memory access speeds were roughly 
equivalent.


But then Cache got faster than main memory.
- Memory optimized indexes performed worse than the B+ trees because they were not cache aware.

Indexes are usually rebuilt in an in-memory DBMS after restart to avoid logging overhead.

### Query Procesing
- In the disk based operating system the disk I/O was always the most expensive thing.
  Who cares how you computed the data, or organize the access of the data once it was in memory.
- In an in-memory based system, we are going to care now the overhead of doing function calls and branches,
  so you need more carefull, how you organize the system and do query processing.
- Sequential scans are also not significantly faster in an in-memory system
  maybe there's certain algorithms to join other things that we don't have to worry making optimal that schedule    access, because random access will be enough.
  
The best strategy  for executing a query plan in a DBMS changes when all of the data  is already in memory.
- Sequential scans are no longera significantly fater than random access.

The traditional **Tuple-at-a-time** iterator model is too slow because of functions calls.
- this problem is more significant in OLAP DBMS

### Logging and Recovery
Now that all is in-memory, there's no dirty pages to flush into disk.
- we can be more conservative
- we can end up recording less data, than we need in a disk based system.
- So standard techiniques like Root camp, we'll use the batch of logs and amortize **fsync**, that's applicable
  to disk based systems too.
- but being able to use a more lightweight logging scheme is a definite advantage for an in-memory system.

No dirty pages-
we don't need to do any undos-
writing into the disk as part of a checkpoint

The DBMS still needs a WAL on non-volatile storage since the system could halt at anytime.
- Use **groupt commit** to batch log entries and flush them together to amortize **fsync** cost.
- May be possible to use more lightweight logging schemes (i.e. only store redo information)

Since there are no 'dirty pages', there is no need to track LSNs  throught the system

### Bottlenecks
If the disk I/O is no longer the slowest resource, what are the other bottlenecks we have to take account of?
- Locking/latching
- Cache-line misses
- Pointer chasing
- Predicate evaluations
- Data Movement & Copying
- Networking (between application & DMBS)

How to deal with these other issues when we design a database system

### Concurrency Control
Concurrency control is the protocol that allows you **execute** multiple **transactions** at the same time.
- And each of these **transactions** are going to have this illusion that they're executing on the system by themself.
- so they don't worry about reading the effects of other transactions occuring at the same time.
  
Provides **Atomicity** + **Isolation** in ACID

For in-memory DBMS, the cost of a **transaction acquiring** a **lock** is the same as accessing data.
- in a disk loading system, all the locks would be stored in memory, kind of data structure. and separated from actual tuples.

The other important thing to understand is that in a disk running system, the stalls are due to transactions trying to access the data that wasn't in memory, so you have to get out to disk and get them.
- now those kinds of stalls are going away.
- yes there are going to be memory stalls, but they are going to be much more infrequent than just stall.

But what we are going to have is a way more cores, and now the contention is going to be in the system of 
many transactions to read and write to the same objects at the same time. And they are not stalling, because there's a disk

New **bottleneck** is contention caused from **transactions** trying to **access data** at the **same time**.

The DBMS can store locking information about each tuple together with its data.
- this helps CPU cache locality
- Mutexes are too slow. Need to use **compare and swap (CAS)** instructions

Mutexes are too slow to protect tuples, instead we are going to use this atomic operation called 'compare and swap'.

### Compare and swap
Compare and Swap is an Atomic instruction that every modern CPU will provide you.
- concept from 1970'
- It's a single instruction that's going to do a look up in a memory location **M**
- And it's going to check if that memory location has a certain value **V** that provided
- If that's value **V** is equal to the value you're checking in then
- you are allowed to install a new value **V'** to update.
- Otherwise, the operation fails

![](10.jpg)

In this example, in c++ with linux libc.
- We are given a memory address, we're giving a compare value and a new value.
- So the current memory address, that **M** points to contains the value 20.
- So in a single instruction, we are going to see whether 20 is equal to 20 
- If yes, install new value 30, otherwise fail.

This is used as a lock free or latch free operation efficiently.

### Concurrency Control Schemes
The two types of categories of concurrency protocols that we are going to work are:

**Two Phase Locking (2PL)**
- Pessimistic scheme, where the data system is going to assume transactions are going to conflict
- And therefore they have required locks on any object before they are allowed to access them.
  
**Timestamp Ordering (T/O)**
- An optimistic scheme, where you assume conflicts are rare,
- so transactions do not need to first acquire locks on database objects
- and instead, check for conflicts at commit time.



### Two Phase Locking
We have a transaction **T1**, and it wants to do is a **read** on **A** followed by a **write** on **B**
- we have to acquire all locks for any object that we want to read or write.
- So we get the **Lock A**  and **Lock B**
- So the first part of the transaction is called the **growing phase**, this is where we are acquiring locks
- And then as soon we **release** one block, now we are in the **shrinking phase**,
- we are **not allowed** to acquire any new locks
- but we can do operations on the only objects we still have all the locks fora
  
![](11.jpg)

Note that in this simple example there's only one type of lock on A and B.
- but in a real system, you have different lock modes. (shared mode, multiple transactions read the same object,
  an exclusive mode) to say only one transaction can lock

In a real system, based on SQL,
- you wouldn't have explicit **lock** and **unlock** commands, those are handled automatically.

Rigorous 2 Phase Locking
- So typically you don't release the locks until the transaction actually commits.

So we are not doing that now, we can unlock 'A', then do the writing on 'B' and still follows the original 
2 Phase Locks Protocol.



Let's say now, we have another transaction **T2**
- it wants to do a **write on B** followed with a **write on A**
- Say that those transactions are running at the same time.

1. In **T1**, we get the **lock on A** while in **T2**, we get the **lock on B**
2. In the next step, **T1** does a **read on A** while **T2** is doing a **write on B**
3. But now we are getting into trouble, because, **T1** wants a **lock on B** while **T2** wants a **lock on A**

![](12.jpg)

So they have to stall.
- They are essentially waiting for the other transaction to give up the lock.
- we have a deadlock, and we need to do something to break this.

#### Deadlock detection
This is where you have a separate background thread, that's just periodically wake up, 
- Check, whether the transactions are running.
- Each transaction maintains a queue of the transactions that hold the locks that is waiting for.
- If deadlocks found, use a heuristic to decide what transaction to kill in order to break the deadlock.
  (i.e. kill the one that has done the less amount of work)
  
#### Deadlock prevention
Instead of having a separate thread, you just have a way to make sure when transaction tries acquire a lock,
they can't hold it, and then it makes a decision about what it should do other than just waiting
- Check wheather another transaction already holds a lock when another transactions request it.
- If Lock is not available, the transaction will either (1) wait (2) commit suicide (3) kill the other transaction

we do make sure we do the operations in the right order so that there's no cycle dependencies.

## Timestamp Ordering
This category uses timestamps to figure out the right order that transactions should be allowed to complete.

**Basic Timestamp Ordering (T/O)**
- we are going to check for conflicts on each read and write,
- and use timestamps to determine wheter there is a conflict
- and then we're going to copy tuples into a private workspace for each transaction as they read them
  to ensure if they go back and read the same tuple again, get the same value.
  Otherwise, you could be reading something that was written in the future and that should't have happened.

Suppose we have a transaction **T1** which **reads on A**, then **writes on B**, and finally **writes on A**
- when the transaction **starts**, we hace to assign the **timestamp**,
  because we're going to use that to determine the serial ordering of transactions.
- There are different schemes you can use, i'm going to use the **logical counter**.
  (hardware clock)
  And we update that counter, every time we start a transaction.
- so the transaction starts, and it's going to give the timestamp 10001

![](13.jpg)

Now inside the database, for every single record we're storing, we are going to maintain two additional
fields.
- Read timestamp: the highest timestamp of the last transaction that successfully read this tuple.
- Write timestamp: the last timestamp of the last time wrote this tuple.
The idea is that these timestamps are always going forward in time.

- So the first thing to do is **read on A**
- So go check the **Write** timestamp and see if whether it's timestamp is greather than ours.
  (meaning we're trying to read something in the future, that we wouldn't allowed to read)
- Next you have to update the **Read timestamp** to check if whether it's timestamp is less than ours
  if it is, we go ahead and update it.

![](14.jpg)

- This is telling to other transactions, that we may want to update this tuple that there's was a transaction timestamp at 10001 that has read it.
- So make sure we don't write something in the past.

- Then we move into **Write on B**
- We first check to see if the write timestamp it's in the future from where we are at
- and therefore we would overriding future data with past data which is not allowed.
- And we check the read time and make sure, someone didn't read this record in the future
- and if we write into they would end up missing it.
- so in this case here, out timestamp checks out for both of these **reads** and **writes**
- and go ahead and update that **write timestamp** field.


![](15.jpg)

And then i'll say that our transaction is passing through a stall.
- it's computing the 1 billionth digit of pi.
- And during this time, a transaction is comming along and modifies **record A**

![](16.jpg)

Now we'll see that we have a real issue, because now when i want to **write A**
- That timestamp is greather than our timestamp **10001**,
- that shouldn't be allowed to do this,
- this would be trying to overwrite a logical record that was updated in the future
- with a physical record in the past.
- So this case is violating the time symbol ordering, and our transaction has to get killed.
- and aboard it and we roll back any changes.

![](17.jpg)


**Optimistic Concurrency Control (OCC)**
First proposed in 1981 at CMU by H.T. Kung

- In addition to copying the things you read into your prior workspace
- You're also going to make copies of any tuples you modify.
- and all your rights go into private workspace.
- and then when you go commit, then you do validation as checked as whether there were any conflicts.
- and if not you can merge all your private workspace changes back into the global database.

- **Store all changes in private workspace**
- **Check for conflicts at commit time and then merge**

Timestamp ordering, scheme where transactions copy data
- read / write into a private workspace that is not visible to other transactions
- when a transaction commits, the DBMS verifies that there were no conflicts.


Here is a simple transaction.
- **Read on A**
- **Write on A**
- **Write on B**
- In our database, we don't need the read timestamp record. Just the **write timestamp**
- When transaction starts, unlike basic timestamping protocol, we're not going to assign a timestamp.
- We are going to make a copy into a **private workspace**

![](18.jpg)

OCC has three phases.
- The first one is the read phase of the transaction.

- So we are going to copy that record into a private workspace, so we always read the record at same value

![](19.jpg)

- Now we do a **Write on A**
- we are not going to modify the global database, but our private workspace

![](20.jpg)

We don't have a **write timestamp** yet, because we didn't have assigned one.
- so we are going to save an infinity
- and we are going to save the value 888

![](21.jpg)

Same happens next with **write on B**
- we copy,
- and timestamp to infinity
- and save new value

![](22.jpg)

So now it's should be time to commit, but we are not doing that yet. There's 2 additional phases

Validate Phase: 
- we look up into the workspace
- see what records we have modified
- and go see if there's either transaction that are still running but have read this data
- and therefore they didn't see our updates because there was in a private workspace
- or there's transactions in the past that i've already commited that have modified this
- therefore we didn't actually see their changes as well.
- Either you are doing backwards validation, (a forward validation we've covered in the introduction class not important right now)
- the basic idea is making sure that transactions are always commiting in the right order

![](23.jpg)

So if we pass the validate phase, no conflicts then we enter the **Write phase**
- we now are finally assigned a timestamp
- and then we update the global database with our changes that we've made from our private workspace
- with our new timestamp
- and then at this point, transactions are considered done and commits.

![](24.jpg)


### Observation
- When there is low contention, optimistic protocols perform better because the DBMS spends less time checking for conflicts.
  (OCC performs better than 2 phase locking)


- At high contentionm, the both classes of protocols degenerate to essentially the same serial execution.
   (only one transaction at a time)

## Concurrency Control Evaluation
