# LECTURE 8: THE PINECONE VECTOR DATABASE SYSTEM

¬ Edo Liberty

https://www.youtube.com/watch?v=8LXotdzX_84&list=PLSE8ODhjZXjbDOFN4U4-Uv95-N8sgzs5D&index=8&t=1501s

- WHAT IT IS A VECTOR DATABASE?
  - THE ANSWER
  - SEMANTIC SEARCH
- VECTOR INDEX
  - A NEW KIND OF SEMANTIC QUERY
  - LOCAL SENSITIVITY HASHING (LSH)

## WHAT IT IS A VECTOR DATABASE?

Today
- Simple objects, text tables, json
- Simple questions - keywords, SQL, filters

Tomrrow
- Complex objects, natural language, images
- Complex questions, meaning similarity


### THE ANSWER
The answer has emerged from deep learning models

Represent your data into semantic vectors, 
- as well as the query

![](1.jpg)

This is already the standard
- encode meaning
- semantic search
  
![](2.jpg)

You already are using it
- google search
- Amazon
- facebook

The query is represented as a semantic vector instead of text

![](3.jpg)

### SEMANTIC SEARCH
Find Zeus's siblings  (dog)

so you would insert first the entire database
- then embed those images
- and do the search
  
![](4.jpg)

## VECTOR INDEX
Recap from machine learning
- the linear classifier

![](5.jpg)

### A NEW KIND OF SEMANTIC QUERY
How to scan the data?

QUERY = CLASSIFIER
- half plane (dot product)
- cone (cosine similirty)
- ball (euclidian distance)

![](6.jpg)


**MAIN IDEA**
same as a regular database,
- but instead of foreign keys, use a semantic vector key.
- better, you have regular primary keys, but indexes are semantic vectors

#### WHY IS VECTOR SEARCH HARD?
As you increase the dimmension, it becomes harder to select a specific position.
- any naive partition of the space is going to break your computer power.
  
![](7.jpg)

The search vectors strongly depends on the type of data that you have

![](8.jpg)

### LOCAL SENSITIVITY HASHING (LSH)
How to partition the space?

Think about 2 points in space
- they have some angle between them

What would happen to your space if you cut the entire space in half
- by a random hyperplane

![](9.jpg)

How likely is, that your random cut is going to split those 2 points
- so they live in different sides of the hyperplane

The answer is exactly proportional to the angle
- if the angle is zero, they will always lie in the same side.
- if the angle is 180º, they will always lie in different sides.
- if they are 90º apart, there would be 50/50 percent.

What Happen if now we split 10 times the space
- each point is then converted into this 2^10, so like 10 bits hash value
- which bakes into this nice property that i can mathematically calculate
  - the probability of 2 points having the exact same hash,
  - based on what's the angle between them.

You can boost that
- instead of hashing every point you hash into a bucket.
- but i'll hash every vector to a bunch of buckets
- and make sure that i have boosted the probability such that
  - if 2 things are close enough (angle-wise)
  - they would colide with high probability
  - that means looking for them in the same bins
  - which is start to looking like a geometric search
  - or like an inverted index
- buckets ids = LSH

![](10.jpg)


### INVERTED FILE (IVF) OR CLUSTERING
it's not very efficient 
- you cut things with random hyperplanes

we can do better using clusters.
- if you take the data that you have, and you cluster it into points that are geometrically closer to each others

![](11.jpg)

In this case you delievered some points that don't match the requirements
- and you have wasted some compute
  
![](12.jpg)

This database is now approximated.
- it don't always return what you expect

Note that i have to compute the dot product of each sample with each center.
- you would have many thousands of centers.
- you might want to use navigation centers.

### NAVIGATION CENTERS
Instead of computing each center
- create this **navigation graph** on points
- you start from a random center
- and move towards centers that improves their proximity

![](13.jpg)

A traversal graph, where each edge is the distance between one center and the next one.
- to efficiently avoid computing that many centroids dot products

It generalizes the idea of a skip list.

However it performs really well in some datasets,
- and poorly in other ones.

![](14.jpg)

### PRODUCT QUANTIZATION (PQ)
![](15.jpg)
