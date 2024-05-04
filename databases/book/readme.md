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
  
##### 6.2.2**RELATIONSHIP SETS**

##### 6.2.3**ATTRIBUTES**



### CHAPTER 7:sRELATIONAL DATABASE DESIGN
