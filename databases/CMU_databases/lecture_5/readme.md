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
