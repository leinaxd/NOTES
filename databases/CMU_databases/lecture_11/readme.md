# LECTURE 11: QUERY EXECUTION (I)

## INTRODUCTION

Part 1 is the basics
Part 2. is Parallel Query execution.

## QUERY PLAN
Is a collection of operators arraged in a tree.
- directed acyclic graph

you can translate the SQL query to,
- some kind of logical plan tree


- Data flows from the leaves up towards the root.
- The output of the root node is the result of the query.
  
![](1.jpg)

For example, the join operator we need to decide its implementation,
- it would be a nested loop join
- or hash join
- or merge join

## TODAY'S AGENDA
- PROCESSING MODELS, how actually we are going to implement the passing of results between queries operators
- ACCESS METHODS, table scans, index scans
- MODIFICATION QUERIES, read, insert, delete queries, retrieve information from database
- EXPRESSION EVALUATION, arbitrary complex expressions in your WHERE clause, PROJECT clause. we need a way to evaluate this expression. 
  adding things, modifying values, comparison. Support arbitrary conditions.

### PROCESSING MODEL
A DBMS **processing model** defines,
- how the system **executes** a particular **query plan**.

Different trade-offs for different workloads

Different ways to passing results between different query operators.
- each operator is implemented in isolation
- we need to move intermediate results between the operators.

APPROACH 1. ITERATOR MODEL
APPROACH 2. MATERIALIZATION MODEL
APPROACH 3. VECTORIZED / BATCH MODEL



#### ITERATOR MODEL
Also called 'VOLCANO' or 'PIPELINE' model.

Each Query Plan operator implements a **NEXT()** function.

On each invocation of the next function,
- the operator if going to return either a **single tuple** or a NULL marker (if there are no more tuples).
  
The operator implements a loop that calls **NEXT()** on it's children,
- to retrieve their tuples and then process them.



