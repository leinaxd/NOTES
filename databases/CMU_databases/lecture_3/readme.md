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

## FILE STORAGE
The DBMS stores a Database as one or more files in the disk.
- Like SQLite (1 file)
- postgreSQL (many files as it doesn't hit the file size limit of the OS)
- the file is unintelligible
- but nonetheless, it is saved in the OS format, ext3/ext4/NTFS. whatever OS writting system provides us.
  
Early systems in 1980 used custom filesystems on **raw** storage.
- So no NTFS, no EXT3/4... the file format was proprietary
- some enterprise DBMS still support this
- you can get as much as a 10% of improvement, but the maintenance cost rises as a rocket.

### STORAGE MANAGER
The storage Manager is responsiblea for maintaining a database's file.
- some do their own scheduling for reads and writes to improve spatial and temporal locality of pages.

Within these files, we are going to organize them as a collection of pages.
- Tracks data read/written to pages.
- Tracks the available space.

#### DATABASE PAGES (I)
A page is a **Fixed size** block of data.
- it can contain **tuples**, **meta-data**, **indexes**, **log records**.
- Most systems do **not mix** page **types**.
- Some systems require a page to be **self-contained**.

Each page is given a **unique identifier**, a page ID
- The DBMS uses an **indirection layer** to **map page ids** to **physical locations** at some offset.

If i lose one page, it doesn't affect any of the other pages.

#### DATABASE PAGES (II)
There are 3 different types of pages in DBMS
- Hardware Page (~3KB)
- OS Page (~4KB)
- **Database page (~512B-16kB)**

By hardware page, we mean at what level the device can guarantee a 'failsafe write'.

![](13.jpg)

The main thing we are going to care about.
- the **harbor page** is the **lowest level** what we do **atomic writes**.
- typically 4kb

EXAMPLE,
- So if you are trying to write 16KB and the system crash in the middle of the operation.
- You might have 8 KB right.

## PAGE STORAGE ARCHITECTURE
Different DBMS manage pages in files on disk in different ways.
- **Heap File Organization** (most common one)
- Sequential/Sorted File Organization
- Hashing File Organization

At this point in the hierarchy we don't need to know anything about what is inside of the pages.

### DATABASE HEAP FILE
A **heap file** is an **unordered collection** of pages where **tuples** that are **stored** in random order.
- CREATE
- GET
- WRITE
- DELETE PAGE
- Must support also iterate over all pages

Need Meta-data to keep track of what pages exists and which ones have free space.

Two ways to represent a heap file.
- Linked list (dumb way, nobodoy uses it)
- Page Directory

Within my file i have a bunch of pages,
- where does this pages exists and whether they have free space or not.

#### HEAP FILE: LINKED LIST
Maintain a **HEADER PAGE** at the beginning of the file that stores **two pointers**.
- HEAD of the free page list.
- HEAD of the data page list.

Each page keeps track of number of free slots in itself

![](14.jpg)

So again, this is a linked list.

It doesn't matter where those pages are stored, whether they're contiguous or not.

And because we need to go possible iterate in reverse order, we need pointers in the way back as well

![](15.jpg)

If it's ordered you might search faster.

well this is a bad idea... going through the entire document for searching your data...


#### HEAP FILE: PAGE DIRECTORY
So we have a special **page directory** now, 
- in the Header of our File
- that's going to maintain the mapping from **Page IDs** to the location of data pages.

![](16.jpg)

We can also maintain a meta-data in this directory.
- so track free space in a particular page

So now when i go to insert some data, i don't have to scan that list.
- i just look up the directory file and get everything that i need.

![](17.jpg)

The DBMS has to make sure that the directory pages are in sync with the data pages.

My hardware can't actually guarantee that i can't write two pages at exactly the same time..
- so let's say that i delete a bunch of data here
- and i want to update my page directory, saying the new amount of free space.
- i write some stuff but **before i write** in down to my directory i **crash**.
- so i read this page is empty/full, but it was actually not.

So later on we will talk about a bunch of mechanisms.
- how to maintain a log
- write some special files so if we crash we would know how to recover from that.

I think this is implemented as a hash table.

Each page is exactly the same size.


-> So why different systems uses differnts pages?
- There are trade offs,
- internally, i have to have this page directory __in memory__.
- but now if i want to represent a larger amount of data with one page ID.
- then that size of that table goes down.

Think of it as the TLB, translation lookaside buffer from a CPU,
- if i'm trying to match all bunch of pages, but my page tables gets really large
- i'm gonna have cache misses.


Also you can put checksums to verify for corrupted pages.

## PAGE HEADER
