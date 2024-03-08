# LECTURE 6: HASH TABLES

Tech talks: google napa, tiledb, bodoSQL


## INTRODUCTION
So today's lecture is going to be about Hash tables and how to use in the DBMS

How to support DBMS execution engine to support read and write data from pages

![](1.jpg)

Two types of data structures
- Hash Tables
- Trees

### DATA STRUCTURES
Many data structures can be used in different places.
- Internal Meta-Data
- Core Data Storage
- Temporary Data Structures
- Table Indexes

Can be used to map pages/tuples into physical locations

You could have group of pages organized into a hash table

They could be used as a temporary datastructure, like during query execution.

There are some operations that you might want to build data structures on the fly, and then use it temporaly.
- for example in a hash join

### DESIGN DECISIONS
**DATA ORGANIZATION**, 
- how is the data physically layed out

**CONCURRENCY**,
- you might have multiple queries running in your system


## HASH TABLES
A hash table implments an **unordered assosiative array** that maps KEYS to VALUES.

It uses a Hash function, to compute an offset into the array for a given key, from which the desired value can be found.

- Space Complexity: O(n)
- Time Complexity:
  - Average O(1)
  - Worst O(n)
 
### STATIC HASH TABLES
The simplest hash table that you can think is:
- Allocate a giant array that has one slot for every element you need to store
- To find an entry, mod the key by the number of elements in the array to find the offset on that array

![](2.jpg)

#### ASSUMPTIONS
You **know** the **number** of **elements** **ahead of time**

Each **key** is **unique**

Perfect Hash Function
- __IF__ KEY_1 != KEY_2 __THEN__ hash(KEY_1) != hash(KEY_2)

#### PRACTICAL HASH TABLE

DESIGN DECISION 1, HASH FUNCTIONS.
- How to map a large KEY space into a smaller domain.
- Trade off between being fast vs collision rate.

DESIGN DECISION 2, HASHING SCHEME-
- How to handle KEY collisions after hashing
- Trade off between allocating a largea hash table vs additional instructions to find/insert KEYS.

## TODAY'S AGENDA
HASH FUNCTIONS
STATIC HASHING SCHEMES
DYNAMIC HASHING SCHEMES

## HASH FUNCTIONS
For any input **Key**, return an **integer** representation of that key.

We don't want to use cryptographic hash functions.

We want something fast with low collision rate.

Examples.
**CRC-64 (1975)**
- used in networking for error detection
**MURMUR HASH (2008)**
- Designed as a fast, geral purpose hash functions
**GOOGLE CITY HASH (2011)**
- Designed to be faster to short keys (<64 bytes)
**FACEBOOK XXHASH (2012)**
- From the creator of zstd compression
**GOOGLE FARM HASH (2014)**
- Newer version of CityHash with better collision rates

## HASH FUNCTIONS: BENCHMARK
- the x-axis is the KEY size
- the y-axis is the throughput

|[](3.jpg)

## STATIC HASHING SCHEMES
What hashing schemes are you going to use

APPROACH 1. Linear Probe Hashing

APPROACH 2. Robin Hood Hashing

APPROACH 3. Cuckoo Hashing

### LINEAR PROBE HASHING
Single giant table of slots.

Resolve collisions by linearly searching for the next free slot in the table.
- To determine whether an element is present, hash to a location in the index and scan for it
- Must store the key in the index to know when to stop scanning.
- Insertions and deletions are generalizations of lookups.


#### INSERTIONS.

Suppose we have the KEY = A with value 'val'
- it's common to store the keys contiguous with the value.
  
![](4.jpg)

When we reach KEY = C,
- we found a collision
- the way we are going to resolve it is by **linear-pro-hashing**.
  i.o.w. Scan linearly forward.
  
![](5.jpg)

You don't need any latches for this operation.
- just do an atomic, swap operation.
- if you fail, just go to the next slot
- the slots are circular
  
#### DELETIONS.

Let's suppose we want to delete C
- but hash(C) points to A
- so move to next slot
- if it matches, then delete C

![](6.jpg)

Suppose now we want to delete D.
- but D was coliding with A,
- then colliding with C
- As C does not loger exits
- you cannot find the position of D, as there are a free slot in the middle of the path
  
![](7.jpg)

There's an issue here.
- How do we know if KEY D doesn't exists or it was bypassed by a deleted key

There are 2 strategies to deal with this.
- APPROACH 1. Tombstone, you insert some reserved value when you delete a key

![](8.jpg)

- APPROACH 2. Movement, you just compact, sliding all values up
But when to stop sliding?
Which key, values moves and which don't?

![](9.jpg)

#### REHASHING
So what you do is to perform a,
- **REHASHING**,
- Basically you reinsert each of the key:values you want to slide.
- so you rehash everything below your deletion.

#### NON-UNIQUE KEYS
Choice 1. **Separated Linked List**
- store values in separate storage area for each key

![](10.jpg)

Choice 2. **Redundant Keys**
- store duplicated keys entries together in the hash table

![](11.jpg)

### ROBIN HOOD HASHING
Variant of linear probing that steals slots from 'rich' keys to give them to 'poor' keys.
- Each key is going to track, the number of positions from where should have been inserted in first place.

If we have a colision we have to scan forward to look for the next empty slot.
- on insert, a key will take the slot of another key,
- if the first key is farther away from its optimal position than the scond

Note we are storing now  the number of jumps from the first position.

![](12.jpg)

![](13.jpg)

Here we have moved KEY D, just because E has a higher number of jumps

![](14.jpg)


Usually this is not as very efficient,
- due to all the branch misses collisions
- with the comparison
- with the excessive copying

## CUCKOO HASHING
Use multiple hash tables with different hash functions seeds.
- on insert, check every table and pick anyone that has a free slot.
- if no table has a free slot, evict the element from one of them and then re-hash it find a new location.

**Looks-ups** and **deletions** are always **O(1)** because only one location per hash table is checked.
- Best open-source implementation is from CMU.

The cuckoo bird will lay their eggs in another bird's nest

Writes are more expensive (multiple hashing)
- but we have faster reads.


For simplicity we are showing 2 hash tables.
- insert A

![](15.jpg)

Suppose now we have a collision
- insert B
- well no problem use table 2
  
![](16.jpg)

Now unlucky us, it present to us a new collision in both tables
- insert B
- but it collides in table 1 and table 2.
- so fix it in table 2, and the value you replace use the other table.

So you are trying to backtrace each register to the other table with the other seed to test luck.

![](17.jpg)

![](18.jpg)

![](19.jpg)

But what happen if the new position for A was taken?
- you end up in a loop,

The solution might be to create a new table with a new seed,
- maybe rehash everything back with that new seed.

you have to keep track of your path, to check if there were a cycle in there
- did you came back to the value you started with?
- where there any internal loop?

## DYNAMIC HASH TABLES
All of the previous hash table require the DBMS to know the number of elements it wants to store.
- otherwise, it must **rebuild** the table if it needs to **grow/shrink** in **size**.

**DYNAMIC HASH TABLES**, We want a way to resize the table on demand.
- Chained Hashing
- Extendible Hashing
- Linear Hashing

### CHAINED HASHING
Maintain a linked list of buckets for each slota in the hash table.

Resolve collisions by placing all elements with the same hash key into the same bucket.
- to determine whether an element is present, hash to its bucket and scan for it.
- Insertions and deletions are generalizations of lookups

You can grow the hash table infinitely by adding new buckets to the linked list

you can still use tombstones, but is much easier to deal with, because nothing needs to be rehashed.

![](20.jpg)

Here we are seeing a collision between hash(A) and hash(C)

![](21.jpg)

So now, it present another collision with hash(D)
- but we can extend our bucket and allocate new memory for it

![](22.jpg)

You now need to maintain a tree.
- you might want to balance the tree
- or sorted


If now i insert a million values, and all of them go inside the same bucket.
- in order to find anything you have to scan this long list.

Is is easier to implement a **concurrent** hash table using **chain hashing** vs **linear probing**?
- no particular reason, we are using atomic comparison before inserting.

### EXTENDIBLE HASHING
Chained hashing approach where we split buckets,
- instead of linked list grow forever.

Multiple slots locations can point to the same bucket chain.

Reshuffle bucket entries on split and increase the number of  bits to examine.
- Data movement is localized to just the split chain.

In the following picture,
- we represent the first 2 bits of the hash values
- we have this global counter, which is telling us, how many bits we need to care about for each page.

![](23.jpg)

Let's find Key A

![](24.jpg)

If we now insert KEY B

![](25.jpg)

Now we want to insert KEY C
- but the problem is that our bucket is now full.
- so we need an incremental **RESIZING**
- Increment our global Counter to 3

![](26.jpg)
  
- and split the bucket into smaller buckets

![](27.jpg)

Also, if you delete elements, you can shrink the list.

Every time you need to add a bit to consider.
- it doubles the size of the Mapping array

### LINEAR HASHING
The hash table maintains a **pointer** that tracks the next bucket to split.
- rather than splitting a particular bucket.
- when any bucket overflows, split the bucket at the pointer location.

Use multiple hashes to find the right bucket for a given key.

Can use different overflow criterion.
- Space utilization-
- Average Length of overflow Chains.

Linear Hashing increments the mapping array incrementaly.
- the resizing happens one bucket at a time.

We are doing this, with multiple hash functions. (2 is sufficient) to find the right bucket.
- we use different overflow criterion,
- when the bucket fills up you can use different conditions to decide when to trigger this.

It gives you a smoother growth policy.

![](28.jpg)

If we want to insert key 17,
- but this bucket is full.
  
![](29.jpg)

We have to perform a split
- we add an overflow bucket.

![](30.jpg)

And now we actually have to perform the splitting.
- The split pointer was pointing at first row
- we are going to add a new slot at the end. (number 4)
- and we define a second hash function.

Then we RERUN all of the keys in the first (pointed) bucket (key 8 and 20)
- 8 stays there.
- while 20 goes into that new bucket we created.
  
![](31.jpg)

And then we are going to advance our split pointer.

now what's going to happen is,
- for all subsequent calls we need to decide if keys are above or below this split point or line.
- If the key is below the line, we use the second hash function

![](32.jpg)

Over time we are going to move the split pointer down

Eventually that overflowed bucked will eventually split.



The idea is,
- Splitting the buckets based on the split pointer will eventually get to all overflowed buckets.
  - when the pointer reaches the last slot, delete the first hash function and move back to the beginning


## CONCLUSION
Fast data structures, that support O(1) look ups that are used all throughout DBMS internals.
- trade off between speed and flexibility

Hash tables are usually now what you want to use for a table indices.

## NEXT CLASS
B+ Trees,
- The greatest data structure of all times
