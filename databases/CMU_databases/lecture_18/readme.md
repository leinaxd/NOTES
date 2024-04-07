# LECTURE 18: MULTI-VERSION CONCURRENCY CONTROL

## OVERVIEW
This lecture is going to be the last one about concurrency control.

Last time, we've talked about a technique of doing Optimistic Concurrency Control
- There some specific algorithms to talk about
  - OPTIMISTIC: Basic Timestamp Ordering and OCC
  - PESSIMISTIC: concurrency control with locking

### ISOLATION LEVELS (I)
beyond the fundamental theory of serializability
- there are some cases where you are going to insert or delete tuples
- in that case there would be some additional issues like phantom
  - that make the result of your query incorrect
  - there are many different potential issues, even without considering phantom
  - that would increase the overhead of the transactions

Many systems allows users to specify the ISOLATION LEVEL
- SERIALIZABILITY, you don't allow phantom and you don't allow any of those conflicts
- In the second level REPEATABLE READS, you actually allow phantom but then you ensure there's no cycle in the dependency graph
- In the next level READ COMMITED, you even allow repeatable reads, enables more schedules but with potentially problematic result
- READ UNCOMMITED, allows anything to happen
  
![](1.jpg)


Depending of what anomally you may allow, we have the following compatibility matrix.

![](2.jpg)

Note that,
- when a system is set to be in a lower isolation level
- then its just possible that the system would have unrepeatable read or phantom
- it doesn't have to have
- some systems even when you specify a lower isolation level, the system actually gives you something stronger

As you are allowing lower isolation levels you can do fewer checks, then allow more potential scheduling of the transactions

### ISOLATION LEVEL (II)
**SERIALIZABLE**
If you are using 2 phase locking as the concurrency control protocol
  - You are going to check for phantoms
  - for example using the index lock we have talked about last class
  - for example strict 2 Phase locking

**REPEATABLE READS**
But then if you only want repeatable reads
- you only need strict 2 PL
- you don't need this Index Lock on the phantom problem

**READ COMMITED**
- you still use strict 2PL
- but you can release the **S**hare lock immediately after you use it
- then you would achieve this read commited isolation level

**READ UNCOMMITED**
- No share locks

### ISOLATION LEVELS (III)
SQL has included Isolation Levels on its standard (SQL-92)

You set a txn's isolation level **before** you execute any queries in the txn.

![](3.jpg)

Not all DBMS support all isolation levels in all execution scenarios.
- Replicated environments


If you don't specify the isolation level, different systems defaults different settings
- notice that only 2 systems defines its isolation level to 'serializable' as default
- just because of performance issues.

For many systems, they don't even provide serializability isolation level
- hard to implement
- restrict performance

![](4.jpg)

