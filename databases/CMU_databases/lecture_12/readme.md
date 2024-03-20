# LECTURE 12: QUERY EXECUTION (II)

## INTRODUCTION
Last class we've discussed
- How to compose operators together into a plan to execute an arbitrary query.
- we've assumed that the queries execute with a single worker (e.g. a thread)
- we will discuss now, how to execute queries using multiple workers.

Remember that we go from a SQL query.
- which gets translated to a logical plan, something with this abstract operators.
- Finally to a physical plan, to describe how we are going to execute each operator.

![](1.jpg)

Again we are not specifying which implementation of the JOIN operation we are using.

### WHY DO WE CARE ABOUT PARALLEL EXECUTION
**FIRST PART. SYSTEM LEVEL.**
parallel execution can give us increased performance.
- **THROUGHPUT**, we can execute more queries in our system draining all available resources
- **LATENCY**, on the other hand we might want to speed up the time a single query is processed.

If you have a transactional workload (OLTP),
- you care more about THROUGHPUT
- you would have a lot of transactions coming in, and you want to execute as many as you can.

If you are in the analytical side workload (OLAP),
- then you care more about LATENCY
- so any long running query, you want to complete as quickly as possible.

**SECOND PART. USER LEVEL.**
What users wants from your application is an increased
- RESPONSIVENESS. What the user sees (e.g. faster web pages)
- AVAILABILITY. 


**THIRD PART. ADMIN LEVEL**
Potentially lower **TOTAL COST OF OWNERSHIP (TCO)** 
- try to use fewer machines
- be more energy efficient


### PARALLEL VS DISTRIBUTED
**PARALLEL DBMS**, means how are we going to execute a single query concurrently
- Resources are physically close to each other
- Resources communicate over high-speed interconnect.
- Communication is assumed to be cheap and reliable.
  
**DISTRIBUTED DBMS**, is the specific case
- Resources can be far from each other
- Resources communicate using slower interconnect.
- Communication cost and problems cannot be ignored.

They share a number of similarities,
- in both cases, the database is spread out across multiple **resources**.
- in both cases, the database appear as a single logical database instance to the application.


## TODAY'S AGENDA
PROCESS MODELS, how we handle concurrent workers in our system.
- how to break up queries execution into multiple concurrent pieces
  
EXECUTION PARALLELISM, how we can achieve execution parallelism using a particular process model

I/O PARALLELISM, also how do we achieve I/O parallelism
- how to leverage parallelism for disk or other store media
  
## PROCESS MODELS
How the system we are building is architected,
- in order to support concurrent request
- from a multi-user application


A **worker**, is the DBMS component that
- is responsible for executing tasks
- on behalf of the client
- and then returning the result to the client.

A worker is not necessary always a thread.

APPROACH 1. PROCESS PER DBMS WORKER
- one process per dbms worker
  
APPROACH 2. PROCESS POOL
- use pools

APPROACH 3. THREAD PER DBMS WORKER
- use threads
  
### PROCESS PER WORKER
Each worker is a **separate** OS **process**
- relies on OS scheduler
- Use Shared memory for global data structures
- A crash in the process doesn't take down the entire system

At a high level, is.
- So the application at the left is going to submit it's request (a query)
- to have executed to the dispatcher layer
- the dispatcher is going to fork off a new process, specifically to handle this query.
- Then this worker is going to manage all of the logic needed to execute the query.
- and its going to communicate back-and-forth the results to the client.

![](2.jpg)

So this worker is going to manage all the reads and writes,
- and the different query operators


Examples
- IBM DB2, postgres, Oracle

![](3.jpg)

So Why these systems are using this system.
- when those systems came out, there weren't really a portable threading library like p-threads (common standars)
- this is a legacy architecture compared to newer options
 
if systems wanted to execute on a bunch of different platforms,
- they would kind of re-implement some threading implementation.




### PROCESS POOL
### THREAD PER DBMS WORKER
