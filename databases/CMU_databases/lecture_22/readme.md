# LECTURE 22: DISTRIBUTED OLTP DATABASES

## OVERVIEW
- DISTRIBUTED OLTP SYSTEMS
- REPLICATION
- CAP THEOREM
- REAL-WORLD SCENARIOS

Last time we have talked about different architectures and design choices.

**SYSTEM ARCHITECTURES**
- Shared everything
- Shared memory
- Shared disk
- Shared nothing

**PARTITIONING / SHARDING**
- Hash
- Range
- Round Robin

- **TRANSACTION COORDINATION**
- Centralized / Decentralized
 
### OLTP VS OLAP
On line Transaction Processing (OLTP)
- Short lived read/write txn
- Small footprint
- Repetitive operations

On line Analytical Processing (OLAP)
- Long-running, read only queries
- Complex joins
- Exploratory queries

### DECENTRALIZED COORDINATOR
When the server application wants to begin a transaction
- a primary node is assigned
- that would handle different request
- as the commit txn as well
  
![](1.jpg)

So how the distributed database is going to determine that its safe to commit.

