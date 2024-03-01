# Lecture 1: Introduction


## Course Overview
- This course is about the design / implementation of DBMS
- This course is not about how to use and administer DBMS -> See CMU 95-703 (Heinz college)

- Database Applications (15-415/615) is not offered this semester

### Course outline
- Relational Databases
- Storage
- Concurrency Control
- Recovery
- Distributed Databases
- Potpourri

### Textbook
**Database  System Concepts**, 7th edition, Silberaschatz, Korth, Sudarshan

### Projects
- build your own database engine from scratch
- each projects builds from the previous one
- we will not teach you how to write in c++17

### Bustub
- Disk based storage
- Volcano style query processing
- Pluggable API
- currently doens't support SQL
- Modular implementation

### database research
Vaccination Database tech talk
db.cs.cmu.edu/seminar2021-dose2
people from
- rqlite
- dbt
- Pinecone
- zerowatt
- [tile]db
- google
- Amazon redshift
- fluree
- arrow
- bodo.ai
- trino
- dremio
- firebolt


## What is a Database
Is an organized collection of inter-related data that models some aspect of real world

Databases are the core component of most computer application

### Database example
SQLite is the most deplot database system, deployed in phones.
- used in chrome and safari to store data
- skype also use sqlite


Let's create a database that models a digital music store, to keep track of artists and albums.
Things we need to our store:
- information about albums
- what albums those artists have released

### Flat file strawman
Store our database as a comma-separated values (CSV) file, that we manage ourselves in our application code.
- Use a separate file per entity
- The application must parse the file each time you want to read/write records

So each row will represent each entity (artist or album)
- each column will represent an individual attribute about that entity

![](1.jpg)





