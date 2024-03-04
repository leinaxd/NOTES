# Lecture 3

## OVERVIEW
- We now understand what a database looks like at a logical level
  - and how to write queries

- We will next learn how to build software that manages a database.

### COURSE OUTLINE
We will cover:
- Relational Databases
- Storage
- Execution
- Concurrency Control
- Recovery
- Distributed Databases
- Potpourri

Now we present the software **stack**
- The base layer is the **DISK MANAGER**
- and we build aditional layers on that.

![](1.jpg)

Each of these blocks corresponds to a self-contained (modular) block of the system.
- Each of them represent an abstraction
- The **upper** levels can **interact** with the **lower** ones.



In this lecture, and the next one, we will deal with the **Disk Manager** block.

## DISK-BASED ARCHITECHTURE
The DBMS assumes that the primary storage location is on **non-volatile disk**.

The **DBMS** components **manage** the **movement** of data between **non-volatile** and **volatile** storage.



### STORAGE HIERARCHY
- The fastest storage are the **CPU Registers**, but also they are the most expensive ones.
- The **NETWORK STORAGE**, is a distributed file system like HDFS
  - Amazon S3

**VOLATILE**, you may loose your data at shutdown
- Random Access, you can access to any random data in one instruction

**NON-VOLATILE**, your data is safe if power is down
- Block Addressable, you can't access individual byte
- Sequential

![](2.jpg)


### ACCEESS TIME
The CPU cache has the fastest access time.

![](3.jpg)

You can actually compare the time scale with the human's second.

### SEQUENTIAL VS RANDOM ACCESS
**Random Access** on non-volatile storage is usually much **slower** than sequential access.

DMBS will want to maximize sequential access.
- Reduce the number of writes to random pages
- so data is stored ins contiguous blocks
- Allocating multiple pages at the same time is called an **extent**

### SYSTEM DESIGN GOALS
- Allow the DBMS to manage databases that **exceed** the amount of **memory available**.
- Reading and Writing to disk is expensive,
  - avoid **Stalls**
- Random Access on disk is usually much slower than sequential access, so the DBMS will want to maximize sequential access.

### DISK ORIENTED DBMS
So at the lower level, we have the disk
- And then we are going to represent this blocks or pages.

![](4.jpg)


**IN-MEMORY**, we are going to have a Buffer Pool.

![](5.jpg)

Also we have an **EXECUTION ENGINE** (or query engine)

---

So the **Execution Engine** is going to make our **request** to our **BUFFER POOL**,
- say hey, **i want to read page 2**

**Page 2** is **not in-memory**, 
1. so you have to look the **PAGE DIRECTORY** from disk to memory

![](6.jpg)

2. Now i can find where is the page 2
- And send it to the Execution Engine to interpret it
  
![](7.jpg)


So what we are focusing from now on is how to get from disk to memory.
- This lecture and the next one, we will focus on what data files goes to disk
- Then we will discuss the Buffer pool
- And finally we will discuss how to actually represent the directory.
  
![](8.jpg)

## WHY NOT USE OS (I)
In OS, how would you make appear that you have **more memory** than you actually do.
- Virtual Memory.

So why would i let my DBMS **manage** all this **virtual memory** instead of letting the **OS** actually do it?

One can use **Memory Mapping** to store contents of a file into a process' address space
- syscall 'mmap'
- takes a **file** on disk, you tell the OS to **map** the file pages **into** the address space for my process.
  - Now i can read and write to those memory locations
  - and if it's not in memory the OS brings it in. (you can write to it)
  - then i can do an Nsync and write it back to disk.
- Essentially you are giving up control of the movement of memory to the operative system

On a high level it looks like this.
- we have a bunch of pages of disk-file
- we have a physical memory
- and the os has its own virtual page memory
  
![](9.jpg)

The application says, hey i want to read **page 1**.
- it looks into the **virtual memory**
- we've got a vault and say this thing is not backed by physical memory
- we have to fetch it out from disk

![](10.jpg)

And now update, our page table to now point to that memory location.

![](11.jpg)

We then repeat the process for **page 3**

![](12.jpg)

And now want **Page 2**, but there's a problem.
- there's no free physical space to put this particular page in.
- so i have to make a decision of which of these pages to remove.

And while i'm doing this, i eventually have the potential to stall the database system 
- i have to stall the thread who requested that old page
- install my new page

There are tricks to prevent to read something that is not in memory
- i have to mitigate the stalls

The OS doesn't know exactly what we are doing,
- it just sees a bunch of reads and writes into two pages.
- doesn't understand the query or the semantics

### WHY NOT USE OS (II)
What if we allow multiple threads to access the **mmap** file to hide page faults stalls?
- This works good enough for read-only access
- it's complicated when there are multiple writers

If we start writing things, it becomes problematic
- Now the **OS** doesn't know that certain pages have to be **flushed** out of disk, **before** other **pages** do.
- we talk about this when we talk about **logging** and **concurrency control**

The OS just says i need to write this out, go ahead and write that down.
- doesn't know if that's an okay thing to do

### WHY NOT USE OS (III)
You can get around this by giving out some hints.
**madvice**, Tell the OS how do you expect to read certain pages. 
- __Sequential__ or __Random access__
- How to prevent pages from the beginning to page out.
**mlock**, Tell the OS that memory ranges cannot be paged out.
- prevent pages to be getting written 
**msync**, Tell the OS to flush memory ranges out of disk
- Just flush

So even memory map is something we want to use in our system,
- many people question why should we have to do all this buffer pool stuff
- so you don't want to do this or you would have performance bottlenecks and correctness problems.

Systems that uses MMAP
- monetdb
- LMDB
- RAVENDB
- levelDB
- elasticsearch
Partially use of MMAP
- mongoDB
- MEMSQL
- SQLite

If i die, in my memorial just write 'andy hated mmap'

### WHY NOT USE OS (IV)
DBMS almost always wants to control things.
- Flushing dirty pages to disk in the right order
- Specialized prefetching
- Buffer replacement policy
- Thread/process scheduling

The OS is not your friend.

## DATABASE STORAGE
**Problem 1**, How the DBMS __represents__ the database in files on disk.
- Today
**Problem 2**, How the DBMS __manages__ its memory and move data from disk.
- Next lecture

## TODAY'S AGENDA
- FILE STORAGE
- PAGE LAYOUT
- TUPLE LAYOUT

How to **organize** the database as a **sequence of pages**?
How we actually are going to **store** inside these files?
What do the **tuples** actually **look like** inside those pages.

