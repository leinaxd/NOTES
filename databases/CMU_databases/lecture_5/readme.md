# Lecture 5: BUFFER POOLS

# INTRODUCTION
How the DBMS manages its memory and move it back-forth from the disk

### DATABASE STORAGE
**SPATIAL CONTROL**,
- Where to write pages on disk
- The goal is to keep pages that are used together often physically close together as possible on disk


**TEMPORAL CONTROL**
- When to read pages into memory, and when to write them on the disk
- The goal is to minimize the number of stalls from having to read data from disk.

### ACCESS TIME 
It's important to find an efficient way to keep things in-memory as much as possible.
![](1.jpg)

### DISK ORIENTED DBMS
- the database file is splitted into a bunch of pages
- there were a directory page who stores all mapings from page ids to physical locations in the file

![](2.jpg)

And there it appears the Buffer pool, to load the pages from disk.
- but first it loads the directory.


### TODAY'S AGENDA
- BUFFER POOL MANAGER, responsible for managing the buffer pool (aka buffer cache)
  - which pages to read in, which pages to evict
- REPLACEMENT POLICIES,
- OTHER MEMORIES POOLS

Types of buffer pools that can exists in the DBMS.


## BUFFER POOL ORGANIZATION
Memory Region organized as an Array of fixed-size pages.

An array entry is called a **FRAME**

When the DBMS **request a page**, an exact **copy** is placed into one of these **frames**

![](3.jpg)



We need one more level of indirection so we now are able to access these pages.
- this is called the **PAGE TABLE**

The **Page Table**, keeps track of pages that are currently in memory.
- also **maintains** additional **meta-data** for each of the pages:
  - Dirty Flag, boolean to mark if the page modified?
  - Pin/Reference Counter, if we want a particular page to remain in memory so you keep track the time

![](4.jpg)

While Page directory keeps track of where the pages resides on disk
The Page Table is going to keep track of where those pages resides in the buffer pool in memory.



If one concurrent query wants to fetch another page, we can run into some concurrency issues.
- so a latch on a position in the page table prevents a concurrent modification

![](5.jpg)

- Once latched, you can ask to the page to be loaded in
- then we can release the latch
  
![](6.jpg)

## LOCKS VS LATCHES
**LOCKS**
- **Protects** the database's logical **contents** from **other transactions**
- Held for transaction duration
- Need to be able to rollback changes

**LATCHES** (aka **MUTEX**)
- Protectst the critical sections of the **DBMS** internal **data structure** from other threads
- Held for operation duration
- Do not need to be able to rollback changes

## PAGE TABLE VS PAGE DIRECTORY
The **page directory** is the mapping from **Paged ids** to **page locations** in the database file.
- all changes must be recorded on disk to allow the DBMS to find on restart.

The **Page Table** is the mapping from **Page IDs** to a copy of the page in **buffer pool** frames.
- This is an in-memory data structure that does not need to be stored on disk.

A transaction is when your query has finished computing and it's commited to disk.

PAGE TABLE is in memory
PAGE DIRECTORY is persisted on disk

### ALLOCATION POLICIES
How are we going to decide which pages are going to exists in our Buffer Pools.

**GLOBAL POLICIES**, make decisions for all active transactions.
- it sees al transactions on one time and going to figure out who are kept and who doesn't

**LOCAL POLICIES**, 
- Allocate Frames to a specific transaction without considering the behavior of concurrent transactions
- still needs to support sharing pages.

Individual transactions are going to allocate/deallocate on a per query basis.
- they are going to think about their own execution plan.

### BUFFER POOL OPTIMIZATIONS
**Multiple Buffer Pools**, utilizes multiple concurrent buffer pools at the same time
**Pre-Fetching**
**Scan Sharing**, across multiple queries
**Buffer Pool Bypass**, bypass buffer pool for individual queries.

#### MULTIPLE BUFFER POOLS
**Logically** the DBMS have just **one Buffer Pool**, but **Physically**, it can be **implemented** **multiple Buffer pools**, with different strategies.
- **Multiple buffer pool instances**, running independently in different machines
- **Per-database buffer pools**, each database can have its own buffer pool
- **Per-page** type **buffer pool**, you can even have different buffer pool at the level of individual pages.

![](7.jpg)

It helps to reduce latch contention and improve locality,
- **less fighting** over managing a single page table.
- Allows you to **specialize** for the needs of individual queries/databases/pages

What the **problem** might be that instead of a **single** Buffer Pool we have **multiple** ones?
- How do you decide how many **space** to allocate each buffer pool?
  - many databases have some know so you can **tune** some parameters.
- Could you have **multiples** of the **same pages** in different buffer pools?
  - yes, tipically one **make sure** that **pages** are **mapped** to a **single buffer pool**
- How do you figure out, which buffer pool the page is going to go to.


Suppose we have 2 buffer pools. 
**APPROACH 1**, Object ID
- When you're storing pages, you store some kind of object id assosiated with it.
- by an object id we mean:
  - Type of page (tuples in a table, page that stores part of the index datastructure, log records)

This way you can split types of pages, into different buffer pools.

![](8.jpg)


**APPROACH 2**, Hashing
- Hash the page id to select which buffer pool to access

so we take the hash function with the 'n' modulo, where 'n' is the number of independent buffer pools we have.

![](9.jpg)


## PRE-FETCHING
The DBMS can also prefetch pages based on a query plan.
- Sequential Scans
- Index Scans

### SEQUENTIAL SCAN

So far we have discusesed that the **Buffer Pool** is going to **fetch** the page once it's **needed**.
- but you can also, **pre-fetch** the **page** in advance.

Imagine we have a query Q1 that wants to start accessing Page 0.
- you fetch page 0 into the buffer pool

![](10.jpg)

Then it moves on to fetch page 1 into the Buffer pool.

Now if this is a sequential scan, 
- Q1 is going to need access to page 2 and 3

![](11.jpg)

So why not allow the DBMS to map thesee pages ahead of time.

![](12.jpg)

We keep this pattern up, and Q1 is never having to wait the disk to end as it's a sequential scan.

### INDEX SCAN
In this query we are asking for values between 100 and 250.
- so we are going to get all the tuples from the pages.

![](13.jpg)

we can use a datastructured called an 'index'
- B trees or B+ trees (binary tree)
- This tree is organized based on the value that we are searching.
- then all values are sorted as follows for that particular attribute.

![](14.jpg)

Rather than having to scan all of the pages in the file, we can just traverse the tree.
- which is going to tell us which pages we need to go and look at.
- all of the leaf nodes have pointers connecting to the pages.

So we do a more intelligent pre-fetching

![](15.jpg)


The difference here against sequential scan,
- we have to know, what are the **accessing patterns** for the query. Requires **High level knowledge**

If we treated the same as the sequential scan, we ended reading pages that we are not actually using it.

How do you know how many resources you should allocate to doing pre-fetching vs normal work?
- there are strategies to mitigate allocating too many pre-fetching resources

There should be pre-fetching in both dimensions?
- both database pages as well as the index pages

if you have just one buffer pool,
- the manager still has to figure out how to balance resources between database files and index files.

you can answer queries entirely by looking at the indexes, not need going to go to the database files.

So what is the number at the bottom of the tree?
- the query was asking for the attribute value between 100 and 250

Is the index built specifically for this query?
- no, indexes are maintained by the system,
- but they can be built to answer many queries.

## SCAN SHARING
