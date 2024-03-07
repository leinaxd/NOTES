# CMU_databases

Pareto rule 20% of the curse cover the 80% of the commonly used skills.
- for 25 length videos, 5 is that 20%, so pay attention to that first 5 lectures.

What is a Database?
What are the database Functions?
- Store Data
  - Data sharding (split data across many devices)
  - What kind of data?
    - structured
    - unstructured
    - time series
- Synchronize users
  - lock file
- Query information
  - Get data Out
  - Structure data in some sense
  - Fast retrieval
  - Fast insertions
  - Visualize, data
- Back up
- local/Web allocated
  - Networking

Tools
- Profiling stages (disk, ram access, network speed)


## Lecture 1: introduction
- course overview
  - course outline
  - Textbook
  - Projects
  - Bustub
  - databaseresearch
- what is a database
  - database example
  - Flat File Strawman
  - Data Integrity
  - Flat File Implementation
- Database Management System
  - Early DBMS
- Data Models overview
  - Data Model
  - Schema
  - Relational
- Data Manipulation Languages (DML)
  - Relational Algebra
    - SELECT
    - PROJECTION
    - UNION
    - INTERSECTION
    - DIFFERENCE
    - PRODUCT
    - JOIN
  - Relational Extra Operators
  - Observation
    - Relational model: Queries
- Conclusion

## Lecture 2: Intermediate SQL
- Relational Languages
  - SQL History
  - Relational Languages
- Today Agenda
  - Example Database
  - Basic Sintax: SELECT
  - Basic Sintax: JOINS
  - AGGREGATES
  - Multiple Aggregates
  - Distinct Aggregates  
  - Aggregates Notes
  - GROUP BY operator
  - HAVING CLAUSE
- STRING operations
  - Pattern Matching
  - Specific String Operations
  - STRING CONCATENATION
- DATE TIME operations
- Output Redirection
  - Output Control
  - LIMIT Control
- Nested Queries
  - Nested Queries Operators
- Window Functions
- Common Table Expressions (CTE)
  - CTE Recursion
- Conclusion
- Homework

## Lecture 3 DATABASE STORAGE I

- Overview
  - Course outline
- Disk based architecture
  - Storage Hierarchy
  - Access Time
  - Sequential Vs Random Access
  - System Design Goals
- Disk Oriented DBMS
- Why Not Use OS (I)
  - Why Not Use OS (II)
  - Why Not Use OS (III)
  - Why Not Use OS (IV)
- Database Storage
- Today's Agenda
- File Storage
  - Storage Manager
    - Database Pages (I)
    - Database Pages (II)
- Page Storage Architecture
  - Database Heap File
    - Heap File: Linked list
    - Heap File: Page Directory
- Page Header
  - Page Layout
    - Tuple Storage
    - Slotted Pages
    - Record IDs
- Example
- Tuple Layout
  - Tuple Header
  - Tuple Data
  - Denormalized Tuple Data
- Conclusion

## LECTURE 4: DATABASE STORAGE (Part II)
- Disk Oriented Architecture
- Log Structured File Organization
  - Log Structured Compaction
- Today's Agenda
  - Tuple Representation
- Data Representation
  - Variable Precision Numbers
  - Fixed Precision Numbers
  - Large Values
    - External Storage
- System Catalogs (I)
  - System Catalogs (II)
  - Accessing to table schema
- Database Workloads
  - Bifurcated Environments
  - Observation
  - Wikipedia Example
  - Wikipedia Example: OLTP
  - Wikipedia Example: OLAP
 - Data Storage Models
   - N-ary Storage Model (NSM)
     - NSM: Summarize
   - Decomposition Storage Model (DSM)
     - Tuple Identification
     - DSM: Summary
     - DSM: History
- Conclusion
## LECTURE 5: BUFFER POOLS
- Introduction
  - Database Storage
  - Disk Oriented DBMS
  - Access time
  - Today's Agenda
- Buffer Pool Organization
  - Locks  Vs Latches
  - Page Table Vs Page Directory
  - Allocation Policies
  - Buffer Pool Optimizations
    - Multiple Buffer Pools
- Pre-Fetching
  - Sequential Scan
  - Index Scan
- Scan (cursor) Sharing (I)
- Scan Sharing (II)
- Buffer Pool Bypass
- Buffer Replacement Policies
  - Least Recently Used Policy
  - Clock Strategy
  - Problems
  - Better Policies: LRU-K
  - Better Policies: Localization
  - Better Policies: Priority Hints
  - Dirty Pages
  - Background Writing
- Other Memory Pools
- Conclusion
- Project Nº1
  - Task 1 - LRU Replacement Policy
  - Task 2 - Buffer Pool Manager
  - Task 3 - Multiple Buffer Pools
