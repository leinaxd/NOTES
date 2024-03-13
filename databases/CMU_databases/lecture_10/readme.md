# LECTURE 10: JOIN ALGORITHMS

## INTRODUCTION
Why do we need to join?

we **normalize** tables in a relational database to avoid **unnecessary** **repetition** of information.
- i.e. students and enrollments
- we could repeat student name, graduation year
- or we can split them out using the relational model where,


We can then use the **join operator** to reconstruct the original tuples without any information loss.

When the NoSQL systems were coming out, they said.
- well joins are slow, we are not having them
- nowadays every system supports some form of join operation

There's one study that found that almost all OLAP systems that found,
- nearly 80% of the query run time is spend doing joins
-> it's really important that we have an efficient implementation.

## JOINS ALGORITHMS
We will focus on peforming **binary joins** (two tables) using __inner equijoin__ algorithms.
- These algorithms can be tweaked to support other joins


In general, we want the smaller table to always be the left table ('outer table') in the query plan.

There are multi-way joins, not very practical to implement.
- they exists primarily in research literature

There are other types of joins,
- Anti Join, elements from one table, doesn't join with elements in the other table
- Theta join, an arbitrary condition for example greather or less than condition
- Inner Equijoin
- Left Outer Join

Techiniques we are going to see can generalize to other types of joins.

we want the smallest table, to be the left (outer) table.
- it's not the fewer the one with fewer number of tuples or records.
- but the table with fewer number of **Pages**

## JOIN OPERATOR
Here we have 2 tables, R and S.
- they have some shared id.
- There are some selection condition filtering values greather than 100.
- we are doing some projection step in the middle
- we are asking for R.id and S.cdate

![](1.jpg)


DECISION 1. Output.
- What's going to be the output of the join operator?
- by output we mean, what the join operator is going to emit ot it's parent operator in the query plan tree.
  
DECISION 2. Cost analysis Criteria.
- How do we determine whether one join algorithm is better than other?

### OPERATOR OUTPUT
Every time we have a tuple $r\in R$ and tuple $s\in S$ when we the join attributes match,
- we need to concatenate **r** and **s** together
- and return a new tuple that represent their joined representation.

What kind of factors go into this decision?
- Depends on processing model,
  - are we returning one tuple at a time or several
  - an array of tuples
- Depends on storage model
  - if we have a row storage model, we can get all the tuple values at once.
  - in the column storage model, we have this late materialization idea,
    - store the key plus a pointer
- Depends on data requirements in query
  - we only need these two columns in the final projection,
  - we could apply an early filtering of attributes (projection push down)

![](2.jpg)


#### OPERATOR OUTPUT: DATA
**EARLY MATERIALIZATION**, 
- copy the values for the attributes in outer and inner tuples,
- into a new output table.

advangages,
- you never have to go back and fetch the columns that you needed
- so no pointers, the data is right there.

disadvantages,
- bad idea for wide tuples, (many columns that you are not going to use)
- excess copying

![](3.jpg)


Subsequent operators in the query, (like the projection) 
- never have to go back to the base table to get more data

Do you store the intermediate result into the Buffer pool?
- yes,

#### OPERATOR OUTPUT: RECORD IDS
**LATE MATERIALIZATION**,
- Only copy the join keys along with the RECORD ID of the matching tuples.
- you want to materialize the data as late as possible so you would be sure you use all the information.

![](4.jpg)

In this example we just need the S.cdate column

![](5.jpg)

Ideal for column stores because the DBMS does not copy data that is not needed for the query.

### COST ANALYSIS CRITERIA
