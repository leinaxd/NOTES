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

**COST BASED SEARCH**
- use a model to estimate the cost of executing a plan
- Evaluate multiple equivalent plans for a query and pick the one with the lowest cost.

