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

APPROACH 1. Linear Probe Hashing

APPROACH 2. Robin Hood Hashing

APPROACH 3. Cuckoo Hashing



