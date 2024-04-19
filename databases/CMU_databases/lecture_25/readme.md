# LECTURE 25: FINAL REVIEW

## OVERVIEW
SQL

BUFFER POOL MANAGEMENT

HASH TABLES

B+TREES

STORAGE MODELS

INTER-QUERY PARALLELISM

### QUERY OPTIMIZATION
Heuristics
- predicate Pushdown
- Projection Pushdown
- Nested Sub queries: Rewrite and Decompose

Statistics
- Cardinality estimation
- Histograms
  - estimate cardinality
    
Cost based search
- dynamic programming, memoize of how to join tables

### TRANSACTIONS
ACID

CONFLICT SERIABILITY
- How to check?
- How to ensure?

VIEW SERIALIZABILITY

RECOVERY SCHEDULES

ISOLATION LEVELS / ANOMALIES

TWO PHASE LOCKING
- Rigorous vs Non rigorous
- Deadlock detection and prevention

Multiple Granularity locking
- intention locks

TIMESTAMP ORDERING CONCURRENCY CONTROL
- Thomas write rule

OPTIMISTIC CONCURRENCY CONTROL
- Read phase
- Validation phase
- Write phase

MULTI VERSION CONCURRENCY CONTROL
- Version storage/Ordering
- Garbage collection

### CRASH RECOVERY
LOGGING AND RECOVERY

BUFFER POOL POLICIES
- STEAL VS NO STEAL
- FORCE VS NO FORCE

WRITE AHEAD LOGGING

LOGGING SCHEMES

CHECKPOINTS

ARIES RECOVERY
- LOG SEQUENCE NUMBERS
- CLRs

### DISTRIBUTED DATABASES
SYSTEM ARCHITECTURES
- shared nothing
- shared disk
- (nodoby uses shared memory)
  
REPLICATION SCHEMES
- SYNCHRONOUS
- ASNYNCHRONOUS
- STRONG/EVENTUAL CONSISTENCY
- PRIMARY REPLICA
  
PARTITIONING SCHEMES
- Range partition
- hash partition
- consistency partitioning
  
TWO-PHASE COMMIT PROTOCOL

### FINAL COMMENTS ABOUT WRITTING DATABASE SYSTEMS FROM SCRATCH
Know your goal, constraints and resources
- Focus on 'high pole in the tent', the most important part, or the worst bottleneck of the system
- Keep remind yourself to reevaluate

Avoid pre-mature optimization/engineering for non-exists requirements
- prefer simpler solutions

Avoid cutting corners
- Balance engineering effort and extensibility

Understand what scenario are you going to deal
