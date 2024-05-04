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

### CHAPTER 7:sRELATIONAL DATABASE DESIGN
