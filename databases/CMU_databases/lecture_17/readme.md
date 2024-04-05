# LECTURE 17: TIMESTAMP ORDERING CONCURRENCY CONTROL


## OVERVIEW
Last time we talked about this canonical concurrency control protocol called 2 phase locking
- also its variant 'strong strict 2 phase locking'

we have talked a little bit of hierarchical locking,
- to acquire locks for tables or pages instead of just records
- to coordinate those locks at different levels we introduced intention locks
  - Intention Shared, we are not locking at the current level, but we lock a few locks below this current level
  - Intention Exclusive, we are not locking anything at the current level, but we lock a few locks below this current level with an exclusive lock
  - Shared+Intention Exclusive, we are going to lock the current level with a shared lock, but in the meantime i may also want to acquire exclusive locks on the levels below
 

### LOCKING PROTOCOL
Each txn obtains appropiate lock at highest level of the database hierarchy.

To get **S** or **IS** lock on a node, 
- the txn must hold at least **IS** on parent node

To get **X**, **IX** or **SIX** on a node, 
- must hold at least **IX** on parent node.

#### EXAMPLE
T1- Get the balance of Lin's bank account
T2- Increase Andrew's bank account balance by 1%

What locks should these txn obtain?
- Exclusive locks + shared for leaf nodes of lock tree
- Special intention locks for higher levels

Then T1 comes alone, wants to read tuple 1.

![](1.jpg)

So first acquire an IS lock for the table
- then it require an S lock for reading tuple 1.

![](2.jpg)

Conversely, T2 arrives and wants to update Andrew's record

![](3.jpg)

so first it has to acquire an intention exclusive lock
- then an exclusive lock in the tuple

![](4.jpg)

**Note** that **IS** is compatible with **IX**


EXAMPLE,
Assume there are 3 txns executing at the same time.
- T1 scan **R** and update a few tuples
- T2 read a single tuple in **R**
- T3 scan all tuples in **R**

So the first transaction tries to read and update a few tuples, 
- so it acquires an **SIX** lock

![](5.jpg)

It follows T2, that wants to read a single tuple in R
- it first acquire a shared intention lock **IS**
- then it acquires a Shared lock **S** on tuple 1
  
![](6.jpg)

Note **SIX** and **IS** are compatible intention locks

Finally T3 comes alone, 
- it wants to scan every tuple in **R**
- it also wants to acquire an **S** lock on table **R**
- but that's incompatible with **SIX** as there's something being updated downhill

![](7.jpg)

### MULTIPLE LOCKS GRANULARITIES
Hierarchical locks are useful in practice as each txn only needs a few locks

Intention locks help improve concurrency:
- Inention shared **IS**, Intent to get **S** locks at finner granularity
- Intention exclusive **IX**, Intent to get **X** locks at finner granularity
- Shared Intent Exclusice **SIX**, Like **S** and **IX** at the same time

### LOCK ESCALATION
Lock escalation dynamically asks for coarsergrained locks,
- when too many low-level locks acquired

This reduces the number of requests that the lock manager must process

The system automatically detect, you have acquired too many tuple locks,
- so better it grants you a table lock

### LOCKING IN PRACTICE
Systems will not allow you to actually specify these locks manually.
- the whole point in database systems is to guarantee the ACID properties
- sometimes you have to provide the DBMS with hints to help it improve concurrency

#### LOCK TABLE
Explicit locks are also useful when doing major changes in the database
- There are different ways to do this in different systems
- Not part of SQL standard

POSTGRES/DB2/ORACLE: **SHARE**, **EXCLUSIVE**
MYSQL: **READ**, **WRITE**

![](8.jpg)

![](9.jpg)

![](10.jpg)

#### LOCK HINTS
It's more common to perform a select,
- and then sets an exclusive lock on the matching tuples

can also set shared locks.
- POSTGRES: FOR SHARE
- MYSQL: LOCK IN SHARE MODE

![](11.jpg)

### CONCURRENCY CONTROL APPROACHES
So far we have talked about 2 Phase concurrency control.
- determine the seriability order of conflicting operations at runtime while executing txns.
- pessimistic,
  - you assume conflicts are going to happen very often
  
Timestamp ordering (T/O)
- determine seriability order of txns before they execute
- Optimistic,
  - you assume conficts are rare

### T/O CONCURRENCY CONTROL
Use timestamps to determine the seriability order of txns.

if TS(Ti) < TS(Tj),
- then the DBMS must enfure that the execution schedule
- is equivlent to a serial schedule where Ti appears before Tj

Note that in some cases,
- you can actually come back and modify the timestamp
- but in most cases the timestamp would be fixed

### TIMESTAMP ALLOCATION
Each txn Ti is assigned a unique fixed timestamp 
- that is monotonically **increasing**.

Let TS(Ti) be a timestamp allocated to txn Ti
- Different schemes assign timestamps at different times during the txn

Multiple implementation strategies
- System Clock
- Logical counter
- Hybrid,
  - common in distributed systems.
  - a Logical counter is fixed in a physical machine.
  - so you would have a fixed clock defined at each of the systems
  - and a logical clock without relying all the systems' clocks to be synced
  
### TODAY'S AGENDA
BASIC TIMESTAMP ORDERING T/O PROTOCOL

OPTIMISTIC CONCURRENCY CONTROL

ISOLATION LEVELS

Note that all these timestamp concurrency control talked in this class will belong to the category of optimistic concurrency control
- they all rely on timestamp to perform the protocol
- but there are also specific implementations called 'basic timestamp ordering protocol'
- and another implementation called 'optimistic concurrency control protocol'
- So name convention is confusing

## BASIC TIMESTAMP ORDERING T/O PROTOCOL
Txns are read and write objects **without locks**, instead:

Every txn when accessing object **X** is tagged with a **timestamp** of the last txn that successfully did read/write.
- it maintain 2 timestamps.
- **W-TS(X)** Write timestamp on **X**
- **R-TS(X)** Read timestamp on **X**

after a read/write operation,
- timestamps gets updated
- if txn tries to access an object 'from the future' it aborts and restart.

### READS
IF **TS(Ti)** < **W-TS(X)**, this violates timestamp order of Ti (with regard to the writter of X)
- Abort Ti
- restart it with a new TS.

ELSE:
- Allow Ti to **read** **X**
- Update **R-TS(X)** to **max(T-TS(X), TS(Ti))**
- Make a local copy of **X**
  - to a private workspace
  - to ensure repeatable reads of X in that **Ti** 


## OPTIMISTIC CONCURRENCY CONTROL

## ISOLATION LEVELS
