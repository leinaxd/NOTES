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
The main advantage of MVCC
- **WRITERS** AND **READERS** Don't BLOCK each other

**WRITERS** and **WRITERS**, do indeed affect each others
  
Say for example you have a writing transaction,
- then when you write a new record
- then if there are other transactions that are still reading the earlier version of this tuple, they are not affected
  - because you are not deleting any records
 

Specifically Read only-txns can read a consistent __snapshot__ without acquiring any lock.
- Use timestamps to determine visibility

When a transaction are trying to access tuples
- it could access tuples at a consistent version at a particular point of time

Easily support **time-travel** queries

A snapshot means, that the transaction is reading the state of a database at a particular time point
- that it can only see the versions of the tuples commited by transactions
- earlier than that, but nothing after.

Note that the SNAPSHOT ISOLATION LEVEL
- is not serializable
- even it won't have the basic conflicts we saw in the concurrency class
  - dirty read, dirty write and writting into the uncommited data
- it would have a problem called Write skew.
- at least is a pretty strong isolation level.

Lastly with this multi-version idea.
- it's also easy to support a type of query called 'time-travel' queries.
- you can ask this query to check the state of the database at a particular point back in time.

This is straightforward
- with different versions
- and with a snapshot isolation

you can easily specify a timestamp,
- and try to read tuples with versions before or exactly at this timestamp

### EXAMPLE (I)
Let's say we have 2 transaction and we are going to look at one record A
- T1 reads A, T2 writes A
- for illustration purpose we will maintain a **version** field
  - in actuality databases don't maintain this field

What a database will maintain are the **begining** and **end** Timestamp
- for each version of a particular Record.
 
![](8.jpg)
  
We are going to assign a timestamp at the begining of the execution
- even thought last class in OCC, we say you only need to produce a timestamp at the validation step

At the begining, we read Record A,
- and because the timestamp of T1 is between the begining and end of this particular record.
- is that you can read the record and continue your schedule

![](9.jpg)

Here T2 comes along, and wants to Write on A
- so instead of overwritting this version 0
- we are going to recreate a new version for this tuple.
- With a different value and different timestamp

![](10.jpg)

Also this earlier version of the database would be updated its end-timestamp

![](11.jpg)

Another thing to note, beyond this beginning and end timestamp
- another thing to have is a **Separate location** to keep track of the status
- of all the transactions,
- whether they have commited or not

![](12.jpg)

If T2 writes a new version of this record A,
- before it commits,
- other transactions depending on this isolation level couldn't really see this version.
- as it's not commited yet.


Here Transaction T1 comes back
- because T1 has a timestamp of 1
- now it wants to read the record A
- but here the timestamp is only between the range 0 and 2

![](13.jpg)

This would not generate unrepeatable reads.

Lastly T1 and T2 commits 

### EXAMPLE (II)
Here T1 is reading A, writting A

![](14.jpg)

Here T1 creates a new version of A
- with a beginning timestamp of 1
 
![](15.jpg)

also it has to modify it previous version timestamp for ending at 1

![](16.jpg)

Later on, T2 comes along, and start by reading tuple A
- then which version is going to read?
- well is going to read the first version, just because we see that in the transaction status table
  - T1 hasn't commited yet
 
![](17.jpg)

Now assume T2 is still writting on A
- for example with a locking protocol
- T2 has to wait T1 to release its lock

![](18.jpg)

Meanwhile T1 continues its execution 
- reading the same record it has previously written by itself
- Then T1 goes commit

![](19.jpg)

Now Lock on A is released.
- T2 can continue its execution writting a new version of A
- and ofc update the previous versioning table

![](20.jpg)

Depending on the isolation level you specify
- under the highest level serializable
  - you may not be able to commit this transaction
- but under the snapshot isolation you actually can commit as well.

### IMPLEMENTATION
MVCC is more than just a concurrency control protocol.
- it completely affects how the DBMS manages transactions and the database

Most of the systems implement this optimization

![](21.jpg)

### DEMONSTRATION
```
# POSTGRES: TERMINAL 1
SELECT ctid, xmin, xmax, * FROM txn_demo;
 ctid | xmin | xmax | id | val
------+------+------+----+-----
(0,1) | 498  | 0    | 1  | 100
(0,2) | 498  | 0    | 2  | 200

SELECT * FROM txn_demo;
  id | val
-----+-----
  1  | 100
  2  | 200
```
The additional 3 fields are 
- ctid = location of this tuple (page_id, slot_number)
- xmin/xmax = begin/end timestamp of this particular tuple
With this is obvious that postgres is using MVCC

All tuples had the same xmin and xmax,
- that means that all those tuples were created in the same transaction with a timestamp of 498
- xmax is just a place holder. 0 or infinity. not an actual value.


we are going to first, 
- look at the tuples for this transaction
```
# TERMINAL 1
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITED;
~# BEGIN
SELECT ctid, xmin, xmax, * FROM txn_demo WHERE id=1;
ctid | xmin | xmax | id | val
-----+------+------+----+-----
(0,1)| 498  | 0    | 1  | 100

SELECT txid_current();
txid_current
------------
499
```

Different transactions ids.
```
# TERMINAL 2
BEGIN TRANSACTION ISOLATION LEVEL READ COMMITED;

SELECT txid_current();
txid_current
------------
500
```

Now we are going to do an update query
- only update the record with the id=1
- so the first record would have 2 versions
```
# TERMINAL 1
UPDATE txn_demo SET val=val+1 WHERE id=1;
SELECT ctid, xmin, xmax, * FROM txn_demo;
 ctid | xmin | xmax | id | val
------+------+------+----+-----
(0,3) | 498  |   0  | 1  | 101
```
Let's see what have we got in terminal 2.
- notice that xmax has changed from 0 to 499
```
SELECT ctid, xmin, xmax, * FROM txn_demo;
 ctid | xmin | xmax | id | val
------+------+------+----+-----
(0,1) | 498  | 499  | 1  | 100
```

Even though the first transaction updated these tuple,
- because the first transaction hasn't commited yet
- the second transaction has a higher transaction, when it comes back it can only see the original version of this record.

What if we select that uncommited tuple explicitly
- it cannot see that record
- even though we know there is a tuple at that location.
- but logically the first transaction hasn't commited yet.
```
# TERMINAL 2
SELECT * FROM txn_demo WHERE ctid='(0,3)';
id | val
---+----
 0 | 0
```

What if i update this tuple again in terminal 2?
- terminal 2 is waiting T1 to release its lock on id=1
```
# TERMINAL 2
UPDATE txn_demo SET val=val+1 WHERE id=1;
... and it waits
```

so go into terminal 1 and commit
```
# TERMINAL 1
commit;
```
Then terminal 2 has updated its command.
```
# TERMINAL 2
commit;
```

we can come back and then select everything out.
- note postgres uses 500 also to denote infinity in the end timestamp
```
# TERMINAL 1
SELECT ctid, xmin, xmax, * FROM txn_demo;
 ctid | xmin | xmax | id | val
------+------+------+----+-----
(0,2) | 498  |   0  |  2 | 200
(0,4) | 500  | 500  |  1 | 102
```

---
**PART 2**

What if we increase the isolation level
```
# TERMINAL 1
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT txid_current();
501
```
```
# TERMINAL 2
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT txid_current();
502
```

Now we are going to update T1
```
# TERMINAL 1
UPDATE txn_demo SET val=Val+1 WHERE id=1 RETURNING txid_current();
txid_current
------------
  501
```
i do the same on terminal 2
- but the second transaction stop, waiting for T1 to commit.
```
# TERMINAL 1
UPDATE txn_demo SET val=Val+1 WHERE id=1;
```

Now we effectively commit T1
```
# TERMINAL 1
commit;
```
but T2 throws an error
```
# TERMINAL 2
ERROR: could not serialize access due to concurrent update
```

---

Final example we will try different isolation levels.

```
# TERMINAL 1
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT ctid, xmin, xmax, * from txn_demo;
ctid | xmin | xmax | id | val
-----+------+------+----+-----
(0,2)| 498  | 0    |  2 | 200
(0,5)| 501  | 0    |  1 | 103
```

```
# TERMINAL 2
BEGIN TRANSACTION ISOLATION LEVEL READ UNCOMMITED;
```

Then we update T2
```
UPDATE txn_demo SET val=val+1 WHERE id=2 RETURNING txid_current();
txid_current
-----------
503
```

```
# TERMINAL 1
UPDATE txn_demo SET val=val+1 WHERE id=1 RETURNING txid_current();
txid_current
------------
504

SELECT ctid, xmin, xmax, * FROM txn_demo;
ctid | xmin | xmax | id | val
-----+------+------+----+-----
(0,2)| 498  | 0    |  2 | 200
(0,7)| 504  | 0    |  1 | 104
```
What we get here, 
- for the first tuple id = 1 it is seen the lastest value that is written
- but then, for the other id=2 value, it doesn't see the updated value.


Meanwhile in the second terminal, we are trying to read all transaction as an uncommited read.
- it should see the transaction done by T1,
  - but as it's not obligated to do so, it gives you a better isolation level
- T1 has a current_id of 504
```
# TERMINAL 2
SELECT ctid, xmin, xmax, * FROM txn_demo;
ctid | xmin | xmax | id | val
-----+------+------+----+-----
(0,6)| 501  | 504  |  1 | 103
(0,6)| 503  | 0    |  2 | 201
```

## MVCC DESIGN DECISIONS
CONCURRENCY CONTROL PROTOCOL

VERSION STORAGE

GARBAGE COLLECTION

INDEX MANAGEMENT

DELETES

### CONCURRENCY CONTROL PROTOCOL
**APPROACH 1** TIMESTAMP ORDERING,
- Assign txns timestamps that determine serial order

**APPROACH 2** OPTIMISTIC CONCURRENCY CONTROL
- Three phase protocol from last class
- modification is to install new versions into the private workspace 

**APPROACH 3** TWO PHASE LOCKING
- Txns acquire appropiate lock on physical version before they can read/write a logical tuple
- Instead of locking a single physical copy of this tuple,
  - you are going to lock the specific version of the tuple that you are trying to access
 
### VERSION STORAGE
How you actually storage those additional versions,
- and how do you actually traverse them
- how do you clean them up

Different physical versions of the same tuple,
- we are going to 'chain' them together using pointers.

in each physical copy of a variant of that tuple, 
- we are going to have a specific field
- where to store a pointer, pointing to the next version of this logical tuple.

The another thing to note is,
- that the index, because in many cases, for example you have a B+Tree index or hash index
- the value of that leaf node (record) in the index would point to the head of this variant chain.

The DBMS uses the tuples' pointer field to create a **version chain** per logical tuple
- This allows the DBMS to find the versions that are visible to a particular txn at runtime
- indexes always point to the 'head' of the chain

Then, there are Different storage schemes
- determine where/what to store for each version

#### STORAGE SCHEMAS
**APPROACH 1** APPEND ONLY STORAGE
- New versions are appended to the same table space
  
**APPROACH 2** TIME TRAVEL STORAGE
- Old versions are copied to separate table space
  
**APPROACH 3** DELTA STORAGE
- The original values of the modified attributes are copied into a separate delta record space
### GARBAGE COLLECTION

### INDEX MANAGEMENT

### DELETES
