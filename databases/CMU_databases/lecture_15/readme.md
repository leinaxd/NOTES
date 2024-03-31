# LECTURE 15: CONCURRENCY CONTROL

## OVERVIEW

The DBMS concurrency control and recovery components permeate throughout the design of its entire architecture

![](1.jpg)

### MOTIVATION
so far we talked about how we execute queries
- but what if the database could have many clients

**LOST UPDATES**, Concurrency control

We both **change** the **same record** in a table at the same time.

**DURABILITY**, recovery

You transfer $100 between bank accounts but there is a power failure
- what is the correct database state?

### PROPERTIES
Based on concepts of transactions with **ACID** properties
- let the developers conveniently handle the data
- without worrying about those values got overwritted by another user

There are different metrics of different properties to worry about

Let's talk about transactions

## TRANSACTIONS
A transaction is the execution of a sequence of one or more operations (e.g. SQL queries)
- on a database to perform some higher level functionality

It is the basic unit of change in DBMS,
- partial transactions are not allowed

### EXAMPLE
Move $100 from Lin's bank account to his promotor's account

Transaction:
- Check whether Lin has $100
- Deduct $100 from his account
- Add $100 to his promotor account

### STRAWMAN SYSTEM
Execute each txn one-by-one as they arrive at the DBMS
- one and only one txn can be running at the same time in the DBMS

Before a txn starts, copy the entire database to a new file and make all changes to that file.
- if the txn completes successfully, overwrite the original file with the new one.
- if the txn fails, just remove the dirty copy.

