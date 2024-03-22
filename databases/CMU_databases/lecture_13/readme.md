# LECTURE 13: QUERY OPTIMIZATION (I)

## INTRODUCTION
Remember that SQL is declarative
- User tells the DBMS what answer they want,
- no how to get that answer


There can be a big difference in performance based on plan is used

### HISTORY
First implementation of Query optimizer from 1970.
- people had argued that the DBMS could never choose a query plan better that a human could write

Many concepts and design decisions from the **system R** optimizer are still used today

### ALGORITHMS

**HEURISTICS** (aka RULES) 
- Rewrite the query to remove inefficient stuff
- These techniques may need to examine a **catalog**
- They do **not** need to examine the **data**

The idea is to approximate what would be a preferred way to execute a query.

**COST BASED SEARCH**
- use a model to estimate the cost of executing a plan
- it uses an enumeration mechanisms to explore different alternatives
- then figure it out the best of those
- Evaluate multiple equivalent plans for a query and pick the one with the lowest cost.

The complex things that you cannot easily deside,
- which 2 tables you are going to draw for first,
- which 2 tables you are going to join next
- whether you should use a soft-merge-join or a loop join or a hash join


Mature systems would have both of those systems in place.
- but some newer databases that are still in the early day early stage of the development
- they usually have the first type just because they are easier.

### ARCHITECTURE OVERVIEW
At this point everything would be kind of abstract.

Let's say you write a SQL query
- when the SQL query first arrives at the database
- you inmediatelly have an option.
  - to look at just the raw string of the query.
  - maybe tweak things a little bit
  - rearrange the position of different tokens
- of course, it would be very difficult at this stage
  - to rewrite the SQL to be at a very efficient form
  - there's not much information in the SQL raw string
- in practice nobody optimize in that early stage of the proccess

![](1.jpg)

People would typically just parse this SQL query
- to an abstract syntax tree.
  (straightforward approach from any compiler course)
- you look at the tokens
- what will be the keywords
- would be tokens for the tables and columns
  
![](2.jpg)

Then you would bind this syntax tree
- with information in the database
- There would be a component in every system called **CATALOG**
  - esentially its metadata about the system
![](3.jpg)
