# LECTURE 20: DATABASE RECOVERY

## OVERVIEW
Last time we talked about logging and recovery mechanisms

Recovery mechanisms are techniques to ensure
- database consistency
- transaction atomicity
- durability despite failures


Recovery algorithms have 2 parts
- Actions during normal txn processing to ensure that the DBMS can recover from failure
- Actions after a failure to recover the database to a state that ensure atomicity, consistency and durability

### CHECKPOINTS
Last time we didn't finished talking about checkpoints

while you are writting the logs,
- to make sure that the database has enough information after a crash
- this logs kinds of grows forever

If the database doesn't do anything with it.
- you may have a year of loggings to recover then

one way to address this is called 'checkpointing'
- you take a consistent snapshot of the content of a database periodically
- you can throw much of the stuff after the checkpoint
- and after when you come back from a crash, then you don't need to look at everything either.

At a higher level you have to follow this 3 steps, the order is important
1. write all your logs currently running onto disk
2. write all the dirty pages into a buffer onto a disk as well
3. write a '<checkpoint>' entry to a log record

Assuming a simple checkpoint strategy
- when we are doing the checkpoint. we stop the entire database.

T1 has commited before the checkpoint, so nothing has to be done
- T2 we have to reapply all the canges of this transaction back to the system, just because it has commited. REDO.
- T3 just because it hasn't finished, you have to rollback all its progress. UNDO.
  
![](1.jpg)

ISSUES
- The DBMS must stall txns when it takes a checkpoint to ensure a consistent snapshot
- Scanning the log to find uncommited txns can take a long time
- Not obvious how often the DBMS should take a checkpoint
  - too fast, degrade runtime performance
  - too slow, recovery time would be higher

### CRASH RECOVERY
Today we are going to talk about what are the recovery algorithms 

### ARIES
Algorithm for Recovery and Isolation Exploiting Semantics

Developed in 1990s for the DB2 DBMS

#### MAIN IDEAS
There are 3 main parts of the algorithm
- the logging part
- after crash aries would re-apply all the changes commited
- Undo phase, to reclaim all those changes that haven't been commited
 
**WRITE AHEAD LOGGING**
- Any change is recorded a in log on stable storage before the database change is written to disk
- Must use **STEAL**+ **NO-FORCE** buffer pool policies

**REPEATING HISTORY DURING REDO**
- On restart, retrace actions and restore database to exact state before crash

**LOGGING CHANGES DURING UNDO**
- record Undo actions to log to ensure action is not repeated in the event of repeated failures
- we have to record, what values has to been before and after.

### TODAY'S AGENDA
LOG SEQUENCE NUMBERS

NORMAL COMMIT AND ABORT OPERATIONS

FUZZY CHECKPOINTING

RECOVERY ALGORITHM



## LOG SEQUENCE NUMBERS

## NORMAL COMMIT AND ABORT OPERATIONS
 
## FUZZY CHECKPOINTING

## RECOVERY ALGORITHM
