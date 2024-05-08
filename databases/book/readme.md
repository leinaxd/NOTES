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


**DEGREE OF THE RELATIONSHIP SET**, the number of entity sets involved in the relationship set.
- **BINARY RELATIONSHIP SET**, relationships that involves 2 entity sets
- **TERNARY RELATIONSHIP SET**,
  - Consider the entity sets 'instructor', 'student' and 'research_project'
  - Each 'research_project' can have multiple 'students' and multiple associated 'instructors'
  - Furthermore, each student working in a 'research project' must have an associated 'instructor'
  - we can relate all three relationships through a ternary relationship called 'proj_guide'
    - A particular 'student' is related to a particular 'instructor' to work on a particular 'project'
      
![](6.6.jpg)

**LUCID CHART NOTATION**
- UML standard

In this notation, we keep attributes inside the entity set.
- note that you can also include constraints (FK, PK) to a particular attribute
- The data type (int, varchar, float) are also possible to be included in the diagram

![](lucid_chart_1.jpg)

![](lucid_chart_2.jpg)

##### 6.3 COMPLEX ATTRIBUTES
For each attribute there is a set of permitted values, called **DOMAIN** or **value set** of that attribute.
- The domain of attribute 'course_id' might be the set of all text strings of certain length.
- The domain of attribute 'semester' might be strings from the set {'fall', 'winter', 'spring', 'summer'}

An attribute can be characterized by the following types.
1. **SIMPLE** and **COMPOSITE** attrutes.
   - They are **simple** attributes if they cannot be divided into subparts.
   - **composites** attributes can be divided into subparts.

For example 'name' could be structured as a composite attribute consisting of
- first_name
- last_name
Or the 'address' may be composed from
- street
- city
- state

Composite attributes help us group related attributes, making the modeling cleaner.

Note also, that a composite attribute may appear as a hierarchy.
- Street can be split into
  - street_number
  - street_name
  - apartment_number

![](6.7.jpg)

3. **SINGLE VALUED** and **MULTI VALUED** attributes.
- **single valued**, student_id refers to only one student ID
- **multi valued**, an 'instructor' may have zero, one or multiple phone numbers.
  - and different 'instructors' may have different number of phones
  - Another example is the amount of 'departments' assigned to that instructor
    
5. **DERIVED ATTRIBUTES**
  - The value of this attribute, can be derived from the values of other related attributes or entities.
  - for example, the 'instructor' might have the attribute 'assigned students',
    - so we can derive this attribute by counting the number of 'student' entities associated to that instructor.
  - Another example is when computing the age, derived from the 'date_of_birth'
The value of the derived attributes, are not stored, but computed when required.


In the following example we show how to represent those attributes in the E-R diagram.
- **composite attribute** 'name' has 'first_name', 'middle_initial' and 'last_name'
- the composite attribute 'address' is defined through a **'hierarchy process'**
  - the 'street' is a composite attribute itself
- **{'phone number'}** denoted in brackets denotes a **multivalued** attribute
- while **'age()'** denotes a **derived** attribute.
  
![](6.8.jpg)


An attribute takes a **'NULL'** value, when an entity does not have a value for it.
- the 'Null' value may also mean 'not applicable' or does not exists for that entity
  - for example, a person without a 'middle_inital' attribute may have that attribute set to Null.
- 'Null' may also designate that an attribute is unknown
  - it may be missing (we don't know it yet)
  - or not known (we don't know even if there exists souch a value)

##### 6.4 MAPPING CARDINALITIES
The idea is to express the number of entities that can be related to another entity
- it can be also used not only to describe binary relationship set, but any number of entities contributing to a relation.

For a binary relationionship set **R**, between sets **A** and **B** the mapping cardinality might be.

- **ONE-TO-ONE**, An entity in **A** is associated AT MOST with one entity in **B** and viceversa.

![](6.9a.jpg)

We draw a line from the relationship set to both entities sets.
- an 'instructor' may advice at most one 'student', and a 'student' may have at most one 'instructor'
  
![](6.11a.jpg)

- **ONE-TO-MANY**, An entity in **A** is associated with ANY NUMBER of entities in **B**.
  - However, An entity **B** can be associated with AT MOST ONE entity in **A**

![](6.9b.jpg)

An instructor may advice many students, but a student may have at most one advisor

![](6.11b.jpg)

- **MANY-TO-ONE**, An entity in **A** is associated with AT MOST one entity in **B**,
  - However, an entity **B** can be associated with ANY NUMBER of entities in **A**

![](6.10a.jpg)

An 'instructor' may advice at most one 'student', but a 'student' may have many instructors

![](6.11c.jpg)

- **MANY-TO-MANY**, An entity in **A** is associated with ANY NUMBER of entities in **B**.
  - Also an entity in **B** is associated with ANY NUMBER of entities in **A**

![](6.10b.jpg) 

An 'instructor' may advice many 'students', and a 'student' may have many 'advisors'

![](6.11d.jpg)

NOTE, that the 'advisor' relationship set can be
- many-to-many, if Any number of students can be advised by any number of instructors
- one-to-one, if the university sets the constraint one advisor per student.
- many-to-one, if one instructor can be avice many students
Thus, the mapping cardinalities can vary on real-world constraints.

**NOTATION**
- We indicate cardinality contraints on a relationship by drawing either a directed line (-->), or an undirected line (---)


The participation of an entity set **E** in a relationship **R** is said to be **TOTAL**
- if every entity in **E** must participate in at least one relationship in **R**
- if every 'student' has to have at least one 'advisor', the participation would be total.
    
The participation of an entity set **E** in relationship **R** is said to be partioal
- if it's possible that some entities **E** do not participate in **R**
- if some 'student' are related with some 'advisor', the participation would be partial.

We indicate total representation by a double line
- each student has to have one advisor.

![](6.12.jpg)

A minimum and a maximum cardinality can also be specified.
- a minimum value of 1,
  - indicates total participation of the entity set in the relationship set
  - each entity occur in at least one for that relationship.
- a maximum value of 1, indicates that the entity partcipates in at most one relationship.
  -  while a maximum value of * means no limit.
  
![](6.13.jpg)

The line between advisor and student 1..1 means that each student must have exactly one advisor.
- the line between 'advisor' and 'instructor' indicates that an instructor can have 0 or more students.
- so the relationship is **one to many** with **total** participation of advisor over 'student'

It's easy to misinterpret that the relation 0..* being 'many to one' while the opposite is correct.

The figure 6.13, could alternatively have been drawn with a **double line** from 'student' to 'advisor'
- and an **arrow** from 'advisor' to 'instructor' in place of the cardinality constraint

In the case of nonbinary relationship sets, we can specify some types of 'many-to-one' relationship
- 'student' can have at most 1 'instructor' on a project
- This constraint must be specified by an arrow pointing to 'instructor' on the edge of 'proj_edge'
- we permit at most one arrow out of a nonbinary relationship set, since more may be misinterpreted. refer to section 6.5.2

##### 6.5 PRIMARY KEY
We must have a way to specify how entities and relationships are distinguished.

###### 6.5.1 ENTITY SETS
Conceptually, **individual entities** are **distinct**.
- However, the **differences** among them must be expressed **in terms** of their **attributes**.
- No two entities in an entity set are allowed to have exactly the same value for all attributes.

The notion of a **key** for a **relation schema**, applies directly to **entity sets**. 
- **a key** for an **entity** is a **set of attributes** that suffice to distinguish entities from each other. 
- **superkey**, **candidate key**, and **primary key** are **applicable** to **entity sets**
  - just **as** they are applicable to **relation schemas**.

###### 6.5.2 RELATIONSHIP SETS
We need a mechanism to distinguish the various relationships of a relationship set.

Let **R** be a relationship set involving entity sets $E1 , ... , En$
- Let $primary-key(Ei)$, denote the **set of attributes** that forms the **primary key** for Ei. 
- Assume that all primary keys attributes names are unique.
- The **composition** of the **primary key** for a **relationship set** depends on the **set of attributes** associated with **R**.

If the **R** has **no attributes** associated with it, 
- then the **set of attributes** describes an individual relationship in set **R**

$key(R) = primary-key(E1 ) \cup \cdots \cup primary-key(En)$

If the **R** **has attributes** $a1 .. am$ associated with it, 
- then the **set of attributes** describes an individual relationship in set **R**

$key(R) = primary-key(E1 ) \cup \cdots \cup primary-key(En) \cup \{a1 ... am \}$



### CHAPTER 7: RELATIONAL DATABASE DESIGN
