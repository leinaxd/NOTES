# LECTURE 16: TWO PHASE LOCKING CONCURRENCY CONTROL

## OVERVIEW
last time we have talked about how transactions are going to execute correctly
- Conflict serializable
  - verify using either 'swapping method' or 'dependency graphs'
  - Any DBMS that says that they support 'serializable' isolation does this
- View serializable
  - no efficient way to verify
  - the instructor doesn't know of any dbms that supports this

Observation
- We need a way to guarantee that all execution schedules are correct (i.e. serializable)
- without knowing the entire schedule ahead of time


Solution
- use locks to protect database objects


### EXECUTING WITH LOCKS
we are assuming that there also be a centralized location that would manage all those locks
- hey, what are the locks currently out there.
- which transaction owns which lock
- which transaction is waiting for a lock
  
Here T1 ask lock for A

![](1.jpg)

Then it comes T2 and ask again a lock for A, 
- which is denied
- and T2 has to wait
  
![](2.jpg)

Once T1 release the lock for A
- that's when the lock manager grant access of A to T2

![](3.jpg)

### TODAY'S AGENDA
LOCK TYPES, definition, set terminology
TWO-PHASE LOCKING, very used algorithm to achieve a concurrency control
DEADLOCK DETECTION + PREVENTION, issues of 2-phase locking
HIERARCHICAL LOCKING, heads up on hierarchical locking

## LOCK TYPES
There's actually 2 types of objects to protect records in the database system
- LOCKS
- LATCHES,
  - you have seen it before, they are
  - protection mechanisms on the internal data structure
  - if multiple threads are trying to acces an B+ index, then you would protect the records, and nodes

![](4.jpg)  

### BASIC LOCK TYPES
**S-LOCK**, Shared locks for reads
**X-LOCK**, Exclusive locks for writes.

![](5.jpg)

### EXECUTING WITH LOCKS
The procedure of the lock manager to grant locks is that,
- while transactions are executing
- if they realize it needs a specific record
- it will first request the transaction manager to grant that lock
- either or update a share lock to a exclusive lock
- after its done, it can release its lock
  

Lock manager updates its internal lock-table
- it keeps track of what transactions hold what locks and what transactions are waiting to acquire any locks

#### RUN THROUGH
Here because T1 needs both Read and Write on A, 
- it would request an exclusive lock

![](6.jpg)

## TWO-PHASE LOCKING
## DEADLOCK DETECTION + PREVENTION
## HIERARCHICHAL LOCKING

