# LECTURE 23: DISTRIBUTED OLAP SYSTEMS

## BIFURCATED ENVIRONMENTS

OLTP to store data

OLAP to process data

![](1.jpg)

## DECISION SUPPORT SYSTEMS 
- aka data warehousing
- aka as data lake (when data is huge)

Applications that serve the management, operation and planning levels of an organization,
- to help people make decisions about future issues and problems by analyzing historical data

Two models for OLAP systems
- **Star schema**
- **Snowflake schema**

### STAR SCHEMA
The data is organized, you have a single **FACT** table
- and many dimension tables, at one level to the fact table

you can actually copy your OLTP schema into the OLAP schema...
- but then it's often beneficial to reorganize your data and put them into a unified form
- so it would queried efficiently

In the star schema, you are only allowed to be 1 layer out of your fact table

![](2.jpg)

One star in the center of the table, and many stars around it

**FACT TABLE**, they are usually recalls the events that are generating in your system.

Let's say you are running the database for sales for Amazon.
- the fact table would contain all the sales.
- This fact table would only have this basic information
  - Foreign references to the dimension table outside
 
For example the foreign keys to a product
- and only in those dimension tables you have those detailed information
  - for example for each product
  - you may have the category product,
  - product name

One benefit of this schema approach is that join would be relative simpler
- The joins would be at most joining 2 tables

There could be some redundancy in the dimension of the table as well


### SNOWFLAKE SCHEMA
In this schema, you have a central fact table that are going to record all the events generated in your system
- but don't have the limitation on how many dimension tables you would have

![](3.jpg)

This way, as there are just a few categories,
- you can normalize that data and then extract the category information


### SUMMARY
**ISSUE 1** NORMALIZATION
- SNOWFLAKE schemas take up **less storage space**
- Denormalized data models may incur integrity and consistency violations

**ISSUE 2** QUERY COMPLEXITY
- Snowflake schemas require more joins to get the data needed for a query
- Queries on STAR schemas will (usually) be faster

### EXAMPLE
Let's say we have a distributed database with 4 partitions
- then we have the following simple join query
- Assuming the query land on the first partition
  - then it would need data from all partitions
  
![](4.jpg)

In the NAIVE approach, 
- you copy all the data into the first partition
- then perform the join in there

Issues
- You have to move a lot of data around
- you might have not enough memory

## TODAY'S AGENDA
- EXECUTION MODELS
- QUERY PLANNING
- DISTRIBUTED JOIN ALGORITHMS
- CLOUD SYSTEMS


## EXECUTION MODELS
## QUERY PLANNING
## DISTRIBUTED JOIN ALGORITHMS
## CLOUD SYSTEMS
