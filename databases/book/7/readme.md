
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
A **database** models a set of entities and relationships in the real world. 
- There are a variety of constraints on the data 
1. 'Students' and 'instructors' are uniquely identified by their ID.
2. Each 'student' and 'instructor' has only one name.
3. Each 'instructor' and 'student' is associated with only one department.
4. Each 'department' has only one value for its 'budget'

a **Legal instance** of a relation is when the instance satisfies all such real-world constraints

##### 7.2.1 NOTATIONAL CONVENTIONS
In discussing algorithms, rather than taking examples we shall need to take arbitrary relations and schemas
- we use **Greek letters** for **sets of attributes** (α, ß).
- We use an **uppercase Roman letter** to refer to a **relation schema**.
  - **r(R)** means that schema **R** is for relation **r**.
  - A **relation schema** is a **set of attributes**,
    - but not all sets of attributes are schemas.
- We use a **lowercase Greek letter** to refer to a **set of attributes**
  - that may or may not be a schema.
- A **Roman letter** to indicate that the **set of attributes** is definitely a **schema**.
- we denote by **K** a set of **superkey** attributes
  - If a **superkey** pertains to a specific **relation** schema,
    - "K is a superkey for R"
- We use a **lowercase name** for **relations**
  - Names are intended to be realistic (e.g., 'instructor'),
  - while in our **definitions** and **algorithms**, we use single letters, like **r**
- The notation r(R) thus refers to the relation r with schema R.
- **r(R)** **refers** both to the **relation** and its **schema**.
- A **relation**, has a particular **value** at any given time refered as "instance of r"
- When it is clear that we are talking about an instance,
  - we may use simply the relation name (e.g., r).

We assume that attribute names have only **one meaning** within the database schema.

##### 7.2.2 KEYS AND FUNCTIONAL DEPENDENCIES
Some commonly used constraints can be represented as 
- keys (superkeys, candidate keys, and primary keys)
  - a **superkey** is a set attributes that uniquely identify a tuple
- functional dependencies


We restate the **superkey** definition
- Given r(R), a subset K of R is a superkey of r(R) 
- if, in any legal instance of r(R),
  - for all pairs t1 and t2 of tuples in the instance of r if t1 ≠ t2,
  - then t1[K] ≠ t2[K].
No two tuples in any legal instance of relation r(R) 
- may have the same value on attribute set K.

Whereas a superkey uniquely identify an entire tuple.
- A **functional dependency** uniquely identify the **values** of certain attributes. 

Consider a relation schema r(R), and let α ⊆ R and β ⊆ R.
- The instance r(R) satisfies the **functional dependency α→β**
  - if **all pairs** of tuples **t1** and **t2** in the instance
    - such that t1[α]=t2[α]
    - it is also the case that t1[β]=t2[β].
- the **functional dependency α → β** holds on **schema r(R)**
  - if every **legal instance** of r(R) satisfies the functional dependency

Using the functional-dependency notation, 
- we say that **K** is a superkey for **r(R)**
  - if the **functional dependency** **K→R** holds on **r(R)** 
  - In other words, for every legal instance of r(R),
    - for every pair of tuples **t1** and **t2** from the instance,
    - when t1[K]=t2[K] is also the case t1[R]=t2[R] (i.e., t1 = t2 ).

**Functional dependencies** allow us to **express constraints** that we cannot express with superkeys. 
- consider the schema 'in_dep'
- the **functional dependency** 'dept_name' → 'budget' holds
- because each 'department' (identified by dept_name) there is a **unique** 'budget' amount
```
in_dep (ID, name, salary, dept_name, building, budget)
```

The pair of attributes can also form a **superkey** for 'in_dep'
  - (ID, dept_name) → (name, salary, building, budget)
    
We shall use functional dependencies in two ways:
1. To **test** instances of relations if they satisfy a given set F of functional dependencies.
2. To specify constraints on the set of legal relations.
  - say that F holds on r(R)

Observe in Figure 7.4 that
- **A → C** is satisfied. 
  - There are **two tuples** that have value **a1** and **c1**
- **C → A** is not satisfied
  - knowing **c2** doesn't define **a2** or **a3**
  - Thus, we have a pair of tuples that t1[C]=t2[C], but t1[A]≠t2[A].    

![](7.4.jpg)

Some trivial functional dependencies are
- **A→A** is satisfied by all relations involving attribute A. 
- **AB → A** is satisfied by all relations involving attribute A. 
  - in general, **α→β** is trivial if **β ⊆ α**. 

**some functional dependencies** may not be **required** to hold
- **room_number→capacity** is satisfied.
- however it is not a real-world constraint
  
![](7.5.jpg)

Because we assume that attribute names have only **one meaning** in the database schema
- if we state that **α → β** holds as a constraint on the database, 
- then **α → β** must hold for any schema **R** such that **α ⊆ R** and **β ⊆ R**, 

Given a set of **functional dependencies** F holds on a relation r(R), 
- it may be possible to **infer** other functional dependencies must also hold
- given a schema r(A, B, C), 
- if functional dependencies **A → B** and **B → C** hold on r, 
  - we may infer **A → C** 

We use notation **F+** to denote the **closure** of the set F.
- the set of **all functional dependencies** that can be **inferred** given the set **F** 

##### 7.2.3 LOSSLESS DECOMPOSITION AND FUNCTIONAL DEPENDENCIES
We can use **functional dependencies** to show when certain **decompositions** are **lossless**
- Let **R1** and **R2** form a **lossless decomposition** of **R**
- if at least one of the following functional dependencies is in F+:
  - R1 ∩ R2 → R1
  - R1 ∩ R2 → R2
if **R1 ∩ R2** forms a **superkey** for either **R1** or **R2**
- the **decomposition** of R is a **lossless decomposition**
- We can use **attribute closure** to test efficiently for **superkeys**

Consider the schema
```
in_dep(ID, name, salary, dept name, building, budget)
```
decomposed into 'instructor' and 'department'
```
instructor(ID, name, dept_name, salary)
department(dept_name, building, budget)
```
The **intersection** of these schemas is 'dept_name'. 
- We see that because **dept_name → dept_name, building, budget** the lossless-decomposition rule is satisfied.

the **test** for **binary decomposition** is a sufficient condition for **lossless decomposition**, 
- it is a necessary condition only if all constraints are functional dependencies. 

- multivalued dependencies can ensure that a decomposition is lossless even if no functional dependencies are present.
  
Suppose we **decompose** a relation schema **r(R)** into **r1(R1)** and **r2(R2)**
- where R1 ∩ R2 → R1
- Then the following SQL constraints must be imposed on the decomposition to ensure consistency
- **R1 ∩ R2** is the **primary key** of **r1** enforcing the functional dependency.
- **R1 ∩ R2** is a **foreign key** from **r2** referencing **r1** ensuring each tuple in r2 has a matching in r1,
  - without which it would not appear in the natural join of r1 and r2 .

If **r1** or **r2** is decomposed further, 
- as long as the decomposition ensures that **all attributes** in **R1 ∩ R2** are in **one** relation,
- the **primary** or **foreign-key** on **r1** or **r2** would be **inherited** by that relation.

#### 7.3 NORMAL FORMS
There are a number of different normal forms that are used in designing relational databases.
##### 7.3.1 BOYCE - CODD NORMAL FORM
One of the most desirable normal forms that we can obtain is Boyce–Codd normal form (BCNF). 
- It eliminates all redundancy that can be discovered based on functional dependencies
- though, there may be other types of redundancy remaining.
###### 7.3.1.1 DEFINITION
A relation schema **R** is in **BCNF** with respect to a set **F** of functional dependencies
- if, for **all functional dependencies** in **F+** where α ⊆ R and β ⊆ R,
  - **α → β** is a **trivial** functional dependency (i.e., β ⊆ α) 
  - or **α** is a **superkey** for schema **R**

A **database** design is in **BCNF** if each relation schemas is in BCNF.

Example of a relational schema **not** in BCNF
- **dept_name → budget** holds
- dept_name is not a **superkey** (a department may have many different instructors). 
```
in_dep (ID, name, salary, dept_name, building, budget)
```
The **instructor** schema is in **BCNF**, as **ID** is the superkey.

Let state a general rule for **decomposing** schemas that are **not** in **BCNF**. 
- Let **R** be a schema that is **not in BCNF**. 
- There is AT LEAST ONE nontrivial functional dependency **α → β**
  - such that **α** is not a **superkey** for R. 
We **replace R** in our design with two schemas:
- **(α ∪ β)**
- **(R − (β − α))**
In the case of **in_dep**, **α = dept_name**, **β = {building, budget}** it would be replaced by
- **(α ∪ β) = (dept_name, building, budget)**
- **(R − (β − α)) = (ID, name, dept_name, salary)**
In this example, it turns out that **β − α = β**.

If the decomposistion is **not in BCNF**, further decomposition is required.

###### 7.3.1.2 BCNF AND DEPENDENCY PRESERVATION
**Consistency constraints** may be seen in several ways
- primary-key
- functional dependencies
- check constraints
- assertions
- triggers

The design has to consider **testing constraints efficiently**.
- If testing a **functional dependency** can be done by **considering** just **one relation**,
- then the cost of testing this constraint is low.
- Decomposition into BCNF can prevent efficient testing of certain functional dependencies.

Suppose that a **student** may have **more than one advisor** 
- but **no more** than **one** from a given 'department'
- Suppose that an **instructor** can be associated with only **one department**, 

One implementation would be a ternary relationship set 'dept_advisor', 
- involving 'instructor', 'student', 'department' 
- that is **many-to-one** from pair ('student', 'instructor') to 'department'

![](7.6.jpg)

The E-R diagram specifies the constraint 
- a 'student' may have **more than one** 'advisor', but at most **one** corresponding to a given 'department'

With this new E-R diagram, 
the schemas for the instructor, department, and student relations are unchanged. 

However, the schema derived from the 'dept_advisor' relationship set is
dept_advisor(s_ID, i_ID , dept_name)

Although not specified in the E-R diagram, 
suppose we have the additional constraint that 
- an 'instructor' can **act as advisor** for only **a** single **department**
- Then, the following functional dependencies hold on 'dept_advisor'
- **i_ID → dept_name**
- **s_ID, dept_name → i_ID**

The first functional dependency follows from our requirement that
- an 'instructor' can act as an 'advisor' for only **one department**

The second functional dependency follows from our requirement that 
- a 'student may have at most **one advisor** for a given 'department'

Notice that with this design, 
- we are forced to **repeat** the 'department' **name**
- once for each time an **instructor participates** in a 'dept_advisor' relationship. 

We see that 'dept_advisor' is **not in BCNF** as 'i_ID' is **not a superkey** 
Following our rule for BCNF decomposition, we get
- (s ID, i ID)
- (i ID, dept name)
Both the above schemas are **BCNF**. 
- In fact, any schema with only two attributes is in BCNF
  
Note, that in our BCNF design, 
- there is no schema that includes all the attributes appearing in the functional dependency
- **s_ID, dept_name → i_ID**
The only dependency that can be enforced on the individual decomposed relations is ID → dept name. 
The functional dependency s ID , dept name → i ID can only be checked by computing the join of the decomposed relations.

Because our design does not permit the enforcement of this functional dependency without a join, 
- we say that our design is **not dependency preserving** 
- Because **dependency preservation** is **desirable**, we consider another **normal form**
  - weaker than BCNF, that will allow us to preserve dependencies. 

That normal form is called the **third normal form**


##### 7.3.2 THIRD NORMAL FORM
##### 7.3.3 COMPARISON OF BCNF AND 3NF
##### 7.3.4 HIGHER NORMAL FORMS
#### 7.4 FUNCTIONAL DEPENDENCY THEORY

