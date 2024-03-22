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

At this point you already know the semantics of the query.
- at a high level you already know what the query is trying to do

The Binder would be
- just a straightforward compiler technique to look at the query
- and then try to understand the syntax of the query

The result of the step we would call,
- the **logical plan** of the query.
- that's where you would start optimization

![](4.jpg)

An important thing to emphasize,
- for one specific query
- there could be multiple possible valid logical plans

For example a multi-way join, 
- A JOIN B JOIN C
- if you specify the join order to be as that one
- at this point it will perform (A JOIN B) JOIN C
- we will not try to order things
- we are not trying to optimize the predicates-

At this point it just gives you a valid logical plan from many possible.

The next step is the tree rewriter,
- its pretty common
- it usually needs to look again the information in the system catalog
- look at what would be the columns and the tables
- and start to apply simple heuristics
- to prune down obvious stupid execution choices
- at this point we are not looking at the data, just the query structure
    
![](5.jpg)

Then after the logical rewrite,
- this optimized logical plan is sent to the **query optimizer**
- it represents the cost based,
  - plan emulation
  - it will be the most complicated step by the way
  - to generate an advanced organization

![](6.jpg)

And with the information,
- system catalog
- Cost Model (statistics about the data)

![](7.jpg)

And lastly this physical plan,
- is sent back to the system to execute

![](8.jpg)

### LOGICAL vs PHYSICAL PLAN
The **optimizer** generates a mapping of,
- a **logical algebra expression** to
- the **optimal** equivalent **physical algebra expression**.

At the physical level,
- there's many choices that the system can explore,
- that the search space is so huge
- different orders of joins
- different methods, (sort-merge join, hash join)

Before we go into these complex organization choices,
- if looking at this high level what this query is trying to do
- if there are simple rules to eliminate the stupid choices
- shrink down the search space as much as possible.
- that will help later the physical enumeration to be much more targeted and much more efficient

Another note is that there would be a 1 to 1 mapping from logical to physical operators,
- table A is going to join table B
- but Not always a 1:1 mapping,
  - a multiple JOIN operator but then ordered by some column
    - if you choose to use a sort-merge join in your physical operator
    - then you can perform the **join** and the **order by**,
      - the two steps together in a single physical implementation

### QUERY OPTIMIZATION IS NP-HARD
This is the hardest part of building a DBMS
- if you are good at this, you would get paid $$$

people starting to look at employing ML to improve the accuracy and efficacy of optimizers.
- IBM DB2 tried this with LEO in early 2000
  - problem called 'cardinality estimation' 
  - they abandon this project,
    - if it work fine,
    - if it doesn't, impossible to fix
    
Microsoft SQLServer's optimizer has more than a million lines of code
  
### TODAY'S AGENDA
HEURISTICS and its RULES:
- RELATIONAL ALGEBRA EQUIVALENCES, 

- LOGICAL QUERY OPTIMIZATION, how do we expand nested queries

- NESTED QUERIES

- EXPRESSION REWRITTING


COST MODEL

## RELATIONAL ALGEBRA EQUIVALENCES
## LOGICAL QUERY OPTIMIZATION
## NESTED QUERIES
## EXPRESSION REWRITTING
## COST MODEL
