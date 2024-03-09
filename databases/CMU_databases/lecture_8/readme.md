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

Observation.
- We have assumed that all the data structure are single threaded
- But we need to allow multiple threads to safely access our dataa structures to take advantage of additional CPU cores and hide disk I/O stalls.

