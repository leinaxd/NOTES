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

### ISOLATION LEVELS SURVEY
A survey across many DBMS about what isolation level you are using in your actual system.
- the most used isolation level is the read commited
  
![](5.jpg)

### ISOLATION LEVELS (IV)
You can actually provide in the SQL-92 standard command to give hints
- on wether a transaction is entirely read-only or not
- if the DBMS knowing the balance that this entire txn is read-only,
  - then it could be a potential organization scheme

**ACCESS MODES**
- **READ WRITE** (default)
- **READ ONLY**

![](6.jpg)

It's not implemented by all systems.
- but you can specified it anyways

## MULTI-VERSION CONCURRENCY CONTROL (MVCC)
We are not talking about a specific concurrency control protocol
- instead what we are going to talk about is actually an OPTIMIZATION
- that many systems would apply
- in combination with 'locking', 'optimistic timestamp', etc

The fundamental Idea of multi-version concurrency control is that
- instead of the database having a centrelized copy of the record

The DBMS maintains multiple **physical** versions of a single **logical** object in the database
- When a txn writes to an object, the DBMS creates a new version of that object
- When a txn reads an object, it reads the newest version that existed when txn started


When every transaction writes a new object
- instead of writting that object in place in the global centralized location

what if we keep all the original records intact
- and just write a new copy of the new records

Then we have a different copies of this records
- and other transactions can read either read the current copy created by myself
- or the older copies

That would allow more flexible scheduling

### HISTORY
Protocol was first proposed in 1978 by MID PHD dissertation

First implementation was Rdb/VMS and InterBase at DEC in early 1980's
- both were by Jim Starkey, co-founder of NuoDB
- DEC Rdb/VMS is now 'Oracle Rdb'
- InterBase was open-sourced as **Firebird**

![](7.jpg)

### OVERVIEW
**WRITTERS** DO NOT BLOCK **READERS**

**READERS** DO NOT BLOCK **WRITERS**

Read only-txns can read a consistent __snapshot__ without acquiring locks.
- Use timestamps to determine visibility

Easily support **time-travel** queries
