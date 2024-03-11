# LECTURE 9: SORTING & AGGREGATIONS


## B+TREE CONCURRENCY CONTROL.

We want multiple threads to read and update a B+TREE at the same time.

We need to protect against two types of problems.
- Threads trying to modify the contents of a node at the same time
- One Thread traversing the tree while the another thread splits/merges nodes.

An observation was, that the first step in our latching algorithm,
- to protect the content of the B+TREE,
- was that we are alwayis going to take this right latch on the **root** node of the tree.
- no matter what you do, you are latching the first node.
- as you scale up the number of threads. it becomes a performance bottleneck.
  
![](1.jpg)

### BETTER LATCHING ALGORITHM
Takes into account the following assumptions,
- Most modifications of the B+TREE will not require a split/merge.
- Instead of assuming that we are going to split/merge, optimistically traverse the tree using read latches.
- If you guess wrong, repeat traversal with pessimistic algorithm


How does this work comparing to the original algorithm.
SEARCH: Same as before.
INSERT/DELETE: 
- Set latches as if for search, get to leaf, and set **W** latch on leaf.
- If leaf is not safe, release all latchesa, and restart the thread using previous insert/delete protocol with write latches.

This approach optimistically assumes that only leaf node will be modified; if not **R** latches set on the first pass to leaf are wasteful.


EXAMPLE 2. DELETE 38.
As sooner we go deep into the tree, we keep getting **R** read latches.
- and release them as sooner you go on step deeper.
- when you get to the leaf, get your **W** write latch,
- and it's safe to delete the value.
  
![](2.jpg)

EXAMPLE 4. INSERT 25
This time, 
- there's no space for key 25 to be inserted.
- we have to split node F.
  
![](3.jpg)

DEADLOCKS ARE NOT ALLOWED, so we have to be careful with our algorithm

### LEAF NODE SCAN
Threads so far, have acquireda latches in a 'top-down' manner.
- A thread can only acquirea a latch from a node that is below its current node.
- If the desired latch is unavailable, the thread must wait until it becomes available

But what if we want to move from one leaf node to another leaf node?


EXAMPLE, T1 wants to find keys less than 4
- we start scanning the root node, and putting a **R** latch on it.
- we move to the C node getting a **R** latch and then releasing the A's one

![](4.jpg)

Now we scan across the leaf nodes to find our final range.

![](5.jpg)

Now have T2, that wants to find keys greather than 1 at the same time T1.

![](6.jpg)

So T1 wants to scans before, 
- while T2 wants to scan forwards
- Each thread wants a latch on the other one.
  
![](7.jpg)

As they are both **R** latches, there's no incompatibility,
- both of them get their respective reading latch

This example works out, 
- but if we have now, arbitrary number of readers and writters at the same time
- you can pretty easily run into these kind of deadlocks.
- in this top-down fashion.

1. Latches do not support **deadlock detection** or avoidance.
  - the only way we can deal with this problem is through coding discipline.

2. The leaf node sibling latch acquisition protocol must support a 'no-wait' mode.

3. The DBMS's data structures must cope with failed latch acquisitions.

Conclusion.
Making a data structure thread-safe is notoriously difficult in practice

We focused on B+TREES, but the same high level techniques are applicable to other data structures


## INTRODUCTION
Course status.
- today we are going to start talking about how to execute queries.

![](8.jpg)

Next four lectures will be.
- Operator Algorithms
- Query Processing Models
- Runtime Architectures
