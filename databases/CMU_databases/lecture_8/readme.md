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
- Need to be able to rollback changes

**LATCHES**,
- Protects the critical sections of the DBMS's internal data structurea from other's threads
- Held for operation duration
- Do not need to be able to rollback changes.
