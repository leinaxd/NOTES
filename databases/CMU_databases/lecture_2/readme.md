# Lecture 2

## Relational Languages
The main idea is to avoid having to tell, exatly to execute a query.
- Write a **declarative** specification of the query.
- The DBMS is responsible for efficient evaluation of the query.
- High end systems have a sophisticated __query optimizer__ that can rewrite queries and search for optimal execution strategies.


### SQL History
- IBM first called 'SQuare' (specify queries as relational expressions)
- Originally developed in 1974 as  'SEQUEL' if IBM system 'R' prototype DBMS
- 'Structured English Query Language' SEQL
- Adopted by Oracle in the 1970


IBM relases a commercial SQL-based DBMS
- system/38 (1979), SQL/DS (1981), DB2 (1983)

ANSI Standard in 1986. ISO in 1987
- Structured Query Language


Current standard is SQL:2016
-> SQL:2016 - Json, polymorphic tables
-> SQL:2011 - temporal DBs, pipelined DML
-> SQL:2008 - Truncation, Fancy Sorting
-> SQL:2003 - XML, Windows, Sequences, Auto-gen IDs
-> SQL:1999 - Regex, Triggers, OO

The minimum language syntax a system need  to say that it supports SQL is SQL:1992


### Relational Languages
**DATA MANIPULATION LANGUAGE (DML)**
- responsible for retrieving and modifying data
  
**DATA DEFINITION LANGUAGE (DDL)**
- How to specify objects, tables, indexes, triggers
  
**DATA CONTROL LANGUAGE (DCL)**
- used for security and access control, which user has which permisson to access and update.

Also includes
- View definition
- Integrity & Referential Constraints
- Transactions

Important: SQL is based on **bags algebra (multi sets)** (duplicated are allowed in the dataset) not **sets** (no-duplicates)
- List, allow duplicates but it has a definite order
- Sets, No duplicates but no order
- Bags, can't have duplicates also unordered


## Today Agenda
- Aggregations + group by
- String / Date / Time operations
- Output Control + Redirection
- Nested Queries
- Common Table expressions
- Window Functions

### Example database
Student - Course database.

![](1.jpg)

Machine 1: **POSTGRESQL**
Machine 2: **MySQL**
Machine 3: **SQLite**

```
// Query
SELECT * FROM student;
SELECT * FROM course;
SELECT * FROM enrolled;
```
#### Basic Syntax: SELECT

![](2.jpg)

The **SELECT** statement, maps to the **PROJECTION** operator.
- filter columns
While the **WHERE** statement, maps to the **SELECTION** operator.
- filter values
  
![](3.jpg)

#### Basic Syntax: JOINS

Which students got an 'A' in 15-721?
- Without the last 'Join' operator, the result would be the carthesian product between grades 'A' and students enrolled in course '15-721'
  
![](4.jpg)


#### AGGREGATES
They are functions that returns a single value from a bag of tuples.

**AVG(COL)**     -> Returns the average col value.
**MIN(COL)**     -> Returns the minimum col Value.
**MAX(COL)**     -> Returns the maximum col value.
**SUM(COL)**     -> Returns the sum of values in col.
**COUNT(col)**   -> Returns the number of values for col.


So the Aggregates Functions can only be used in the **SELECT** output list.
- actually there are a few exceptions.
  
![](5.jpg)

- The Percent symbol '%' means to match any regular expression, is the star '*' for re.
- Instead of a specific column, you are free to use the star operator to count all rows
- Also putting a count(1) means to use column number 1 to count.
- All things should be optimized later (specialy for the star operator), so you are safe to use it.

#### Multiple Aggregates
You can actually compute many agregates at a time

![](6.jpg)

#### Distinct Aggregates
To depict which tuple columns are unique

![](7.jpg)

#### Aggregates Notes

Output from other columns outside of an aggregate is undefined.
- e.cid is a table, while AVG is scalar. size missmatch.
  
![](8.jpg)


#### GROUP BY operator
Let's try to fix the last undefined example.

We are going to project tuples into individual subsets
- and calculate aggregates against each subset.

![](9.jpg)

The way we compute this is,
- First compute the join operator
- and then we compute aggregates by those groups

![](10.jpg)


So the rule is.
- Non-aggegated values in the **SELECT** clause must always appear in the group by clause.

![](11.jpg)

#### HAVING CLAUSE
Filters results based on aggregation computation 
- (like a **WHERE** clause for a **GROUP BY**)

This for example would work
- The time the WHERE clause is evaluated, we're not going to know yet, what the avg_gpa is

![](12.jpg)

Now this is basically saying to filter results after gruoped aggregation gets computed.
- Also this syntax isn't standard
  
![](13.jpg)

So you have to duplicate the aggregation clause.

![](14.jpg)

![](15.jpg)

### STRING operations
- The only one that is case insensitive is MySQL
- Strings should be single quoted
  
![](16.jpg)


#### PATTERN MATCHING
**LIKE** clause is used for  string matching.
- **'%'**, matches any substring (including empty ones)
- **'_'**, match any one character

![](17.jpg)

#### SPECIFIC STRINGS OPERATIONS
Many DBMS have their own unique functions

![](18.jpg)

is an empty string the same as null? almost always the answer is no.


#### STRING CONCATENATION
SQL standards defines the '||' operation to concatenate strings.

![](19.jpg)

```
# postgresql also sqlite
SELECT 'data' || 'base' AS strcat;

strcat
------
database
(1 row)
```

```
# mysql
SELECT 'data' || 'base' AS strcat;
ERROR

SELECT 'data' + 'base' AS strcat;
ERROR

SELECT CONCAT('data', 'base') AS strcat;
+----------+
| strcat   |
+----------+
| database |
+----------+
```

## DATE TIME operations
Operations to manipulate and modify **DATE**/**TIME** attributes.
- can be used both in input and output predicates

DEMO: Get the number of days since the begining of the year.
- YYYY-MM-DD
```
# Postgres

SELECT NOW();
    now
-------------
2021-09-01 20:04:39.763535+00

SELECT EXTRACT(DAY FROM DATE('2021-09-01'))
     date_part
--------------------
             1
     (1 row)

SELECT DATE('2021-09-01') - DATE('2021-01-01') AS DAYS;
     DAYS
--------------------
     243
    (1 row)
```

MySQL date computation is weird, review this.

```
# MySQL
SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2021-09-01 20:04:47 |

SELECT DATE('2021-09-01*) - DATE('2021-01-01') AS DAYS;
+----------+
|  DAYS    |
+----------+
|  800     |
+----------+

SELECT ROUND((UNIX_TIMESTAMP(DATE('2021-09-01')) -UNIX_TIMESTAMP(DATE('2021-01-01'))) / (60*60*24), 0) AS DAYS;
+----------+
|  DAYS    |
+----------+
|   243    |
|----------+

SELECT DATEDIFF(DATE('2021-09-01'), DATE('2021-01-01')) AS DAYS;
```


```
# SQLite
SELECT NOW(); ERROR

SELECT CURRENT_TIMESTAMP;
CURRENT_TIMESTAMP
-----------------------
2021-09-01 20:05:13

SELECT DATE('2021-09-01*) - DATE('2021-01-01') AS DAYS; ERROR

SELECT julianday(CURRENT_TIMESTAMP) - julianday('2021-01-01');

julianday(CURRENT_TIMESTAMP) - julianday('2021-01-01')
---------------------------------------------------------
243.839421296492



SELECT CAST(julianday(CURRENT_TIMESTAMP) - julianday('2021-01-01') AS INT) AS DAYS;
DAYS
------
243
```

