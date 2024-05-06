# DATABASE SYSTEM CONCEPTS (A. Silberchatz)

## PART 2: DATABASE DESIGN
### CHAPTER 6: DATABASE DESIGN USING THE E-R MODEL

#### 6.1.1: DESIGN PHASES
1. Specification of user **REQUIREMENTS**
  - There are techniques for diagrammatically represent user requirements 
2. **DATA MODEL**, (aka conceptual design)
  - Translate the requirements into a database schema
  - Typically it is a graphic representation of the schema
3. Specification of the **FUNCTIONAL REQUIREMENTS**
  - types of operations, types of transactions
  - modifying/updating data, searching and retrieve data
The following 2 steps translate the abstract model into its implementation
4. **LOGICAL DESIGN**
  - the designer maps the conceptual schema onto the data model (typically relational)
  - mapping the conceptual schema defined with the Entity-Relation model into a **relation schema**
5. **PHYSICAL DESIGN**
  - The designer uses the system specific database schema
  - the physical features of the database are specified
    - Indexes structures, File Organization
**Note**
- The Physical schema can be changed relatively easy after an application has been built
- However changes to the logical schema are usually harder to carry out,
  - may affect a number of queries, updates

#### 6.1.2 DESIGN ALTERNATIVES
**ENTITY**: Is the type representation of an object
  - people, places, products
  - They are distinct

In designing a database schema, we must ensure that we avoid 2 major pitfails.
1. **REDUNDANCY**, don't repeat yourself
  - i.e. don't repeat attribute 'title' in 'book' and 'sold' entities, use a foreign relation instead
  - ISSUE: redundancy may lead to inconsistencies
2. **INCOMPLETNESS**,
    - bad design may lead to certain aspects of the enterprise unmodeled
    - i.e. entity 'courses offered' may be a bad design for representing all courses available. a better entity would be just 'courses'

Other decisions
- Consider a customer buying a product.
  - is the sale itself an entity?
    - that is related both the customer and the produc

#### 6.2 THE ENTITY-RELATIONSHIP MODEL
Developed to facilitate the logical design of an enterprise schema.

##### 6.2.1**ENTITY SETS**
- Distinguishable object
- Each entity has a set of properties
- The values for some set of properties must uniquely identify an entity
The entity may be concrete (book, person) or it may be abstract (course, flight reservation)

An entity set is a set of entities of the same type
- that shares the same set of properties

**Extension** is used to refer to the actual collection of individual entities belonging to the entity set.

Entity sets don't need to be disjoint
- it is possible to define the entity set 'person' consisting of all people in the university.
  - but also a student or instructor may be related to a person.

An Entity is represented by a set of **attributes**
- Attributes are descriptive properties possesed by each member of an entity set.
- The designation of an attribute, expresses to the database, to store similar information of each entity.
- However each entity may have different values for each attribute
- i.e. ID, name, dept_name, salary
- in section 6.3 we discuss attributes that are composited like 'full name' or multivalued

Each entity has a **value** for each of its attributes
- Historically the governament ID was used to identify persons in companies
- but it is considered a bad practice for security and privacy reasons
- for instance, each company has to define its own identification number.

**REPRESENTATION**
- An entity set is represented in the E-R diagram with a **rectangle**
- which is divided into 2 parts, 1. the name of the entity set. 2. the name of all the attributes
- Attributes that are assosiated with the primary key are underlined.

![](6.1.jpg)

##### 6.2.2 **RELATIONSHIP SETS**
A **relationship** is an association among several entities.
- for example an 'advisor' may asociate instructor 'Katz' with student 'Shankar'

A **Relationship set** is a set of relationships of the same type.

A **Relationship instance** is an E-R schema 
- representing an association between the named entities in the real world enterprise that is being modeled

![](6.2.jpg)

A relationship set is represented by a **DIAMOND** in the E-R diagram.
- which is linked with lines to a number of different entity sets.
  
![](6.3.jpg)

Formally, a **relationship set**
- Let $E_1 .. E_n$ be entity sets that **participate** into the relation.
- Then a Relationship set **R** is a subset of $\{(e_1 .. e_n ) | e_1\in E_1 .. e_n \in E_n\}$
  
$R \subseteq E_1 \times \cdots \times E_n$

The Function that an entity plays in a relationship is called a **ROLE**
- Since the __participation__ of __entity sets__ into a __relationship__ is generally distinct, roles are not specified.
- However, when the same __entity set__ __participate__ more than once into the same __relation__, **explicit roles** have to be given.
  - aka **recursive relationship set**
  - There has to be specified, how an entity participates in a relationship instance.

Consider the entity set '__course__'.
- some couse C1 may be prerequisite for another course C2.
- so we define a relationship set 'prereq',
  - characterized by pairs (C1, C2)

In the E-R diagram, Roles are **labels** into the relationship lines

![](6.4.jpg)

A relationship may also have **descriptive attributes**
- Consider the relation set '__takes__' which relates entity sets 'student' and 'course'
- we may wish to store a descriptibe attribute named 'grade' altogether with the relationship
- An attribute of a relationship set is represented by an **undivided rectangle** connected with a **dashed line** to its diamond representation.

![](6.5.jpg)

A relationship set may have multiple descriptive attributes
- for example 'for_credit' to record whether a student is section for credit or it's just auditing it.

**NOTE**, about multi-page diagrams
- It is a common practice to specify __relationship sets__ attributes in a diagram different from the __entity set__ one.
- Attributes of entities are specified first, but then they are ommited to avoid inconsistencies.


**NOTE**, about relationship sets.
- it is possible that many relationships apply to the same set of entities sets.
- for example 'teaching_asistant' may be also a relation between 'student' and 'courses'

In the formal definition we saw that a set cannot have duplicates,
- if follows that a particular student, can only have one association with a particular 'course'
- so that student can have only one 'grade' for that particular course.

However, if we want to allow the student to have multiple grades to the same course,
- we may have the attribute 'grade' to actually be a 'set of grades'
- souch attributes are called **MULTIVALUED ATTRIBUTES**
- 

**LUCID CHART NOTATION**
- UML standard

In this notation, we keep attributes inside the entity set.
- note that you can also include constraints (FK, PK) to a particular attribute
- The data type (int, varchar, float) are also possible to be included in the diagram

![](lucid_chart_1.jpg)

![](lucid_chart_2.jpg)
##### 6.2.3 **ATTRIBUTES**



### CHAPTER 7:sRELATIONAL DATABASE DESIGN
