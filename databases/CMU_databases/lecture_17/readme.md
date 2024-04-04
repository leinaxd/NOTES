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

  
### TODAY'S AGENDA
