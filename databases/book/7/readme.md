
### CHAPTER 7: RELATIONAL DATABASE DESIGN
The goal of a relational design is 
- to generate a set of relation schemas without unnecessary redundancy
- to retrieve information easily
  - in an appropriate normal form.

In this chapter, 
- we introduce a **formal** approach to **relational** database design 
- based on the notion of **functional dependencies**
- We then define **normal forms** in terms of **functional dependencies** and other types of data dependencies.

#### 7.1 FEATURES OF GOOD RELATIONSHIP DESIGNS
It's possible generate a set of relation schemas directly from the E-R design. 
- The **goodness** of the resulting set depends on how good the **E-R design** was in the first place. 

```
#Figure 7.1 Database schema for the university example.
in_dep (ID, name, salary, dept_name, building, budget)
classroom(BUILDING, ROOM_NUMBER, capacity)
department(DEPT_NAME, building, budget)
course(COURSE_ID, title, dept name, credits)
instructor(ID, name, dept_name, salary)
section(COURSE_ID, SEC_ID, SEMESTER, YEAR, building, room number, time slot id)
teaches(ID, COURSE_ID, SEC_ID, SEMESTER, YEAR)
student(ID, name, dept name, tot cred)
takes(ID, COURSE_ID, SEC_ID, SEMESTER, YEAR, grade)
advisor(S_ID, i_ID)
time slot(TIME_SLOT_IT, DAY, START_TIME, end time)
prereq(COURSE_ID, PREREQ_ID)
```
Suppose that we had started out when designing the university with the schema **'in_dep'**
- as the join between 'instructor' and 'department' 
- This seems a good idea as uses fewer joins for some queries
  - but we have to repeat information once for each 'instructor' in the 'department'. 
  - For example, 'Computer Science', is included in the tuples of Katz, Srinivasan, and Brandt
  - All these tuples has to agree in the 'budget' amount otherwise would be inconsistencies.
    
In our original design using 'instructor' and 'department'
- we stored the amount of each 'budget' exactly once

Even if we decided to live with the redundancy problem, 
- we cannot represent a new 'department' unless it has at least one 'instructor' 
  - as the 'in_dep' table require values for ID, name, salary

![](7.2.jpg)

##### 7.1.1 DECOMPOSITION
To avoid repetition-of-information you can decompose its schemas
- 'in_dep' is decomposed into 'instructor' and 'department'

Not all decompositions are helpful.
- When all schemas consist of one attribute
- No interesting relationships may be expressed.

Now consider a less extreme case where we decompose the 'aemployee' schema
```
employee(ID, name, street, city, salary)
```
into the following schemas
```
employee1(ID, name)
employee2(name, street, city, salary)
```
The flaw in this decomposition arises from the possibility that two employees has the same name. 

The two original tuples appear in the result 
- along with two new tuples that **incorrectly** mix data values

![](7.3.jpg)

**lossy descomposition**
Although we have more tuples, we actually have less information in the following sense. 
- We can indicate that a certain street, city, and salary pertain to someone named Kim,
- but we are unable to distinguish which of the Kims


##### 7.1.2 LOSSLESS DECOMPOSITION
Let R be a relation schema and let R1 and R2 form its decomposition

The decomposition is **lossless** 
- if there is no loss of information by replacing **R** with **R1** ∪ **R2**.
- if for all legal instances, relation r contains the same set of tuples as the following query result
```
SELECT * FROM (SELECT R1 FROM r) NATURAL JOIN  (SELECT R2 from r)
```
This is stated more succinctly in the relational algebra as:
- if we project r onto R1 and R2
- Then compute the natural join of the projection results, we get back exactly r.
$Π_R1(r) ⋈ Π_R2(r) = r$

Conversely, a **decomposition** is **lossy** 
- if when computing the natural join of the projection results,
- we get a proper superset of the original relation. 
$r ⊂ Π_R1 (r) ⋈ Π_R2 (r)$

It may seem **counterintuitive** that we have **more tuples** but **less information**
- As it's unable represent the connection between a name and an address

##### 7.1.3 NORMALIZATION THEORY
**NORMALIZATION**, 
- The goal is to generate a set of relation schemas
- that allows us to store information without unnecessary redundancy,
- yet also allows us to retrieve information easily.

The approach is decide if a given relation schema is in 'good form'
- If it's not then we (lossless) decompose it into a number of smaller relation schemas,
- each of which is in an appropriate normal form.

#### 7.2 DECOMPOSITION USING FUNCTIONAL DEPENDENCIES
##### 7.2.1 NOTATIONAL CONVENTIONS
##### 7.2.2 KEYS AND FUNCTIONAL DEPENDENCIES
##### 7.2.3 LOSSLESS DECOMPOSITION AND FUNCTIONAL DEPENDENCIES
#### 7.3 NORMAL FORMS


