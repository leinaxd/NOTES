# Lecture 11: Edge linking and line detection

How to describe those edges mathematically.
- search for long straight lines


Edge Linking
- Connect edges with similar orientation

Edge searching
- Start with edge pixels and correspond M(x,y) a(x,y)
- locates a boundary box around that pixel (window) 


Find neighbor pixels
- Link pixels if the difference in magnitude is beyond some threshold
- And same for angle

![](edge_linking_1.jpeg)

Boundary Following
- We have edge points around a closed contour 
- 
![](boundary_following.jpeg)

Moore's algorithm for Boundary following
0. Initial position: 1 = Edge position, 0=None
1. Let the starting point b0 be the uppermost, leftmost point labeled '1'
2. Let c0 be the left neighbor of b0

![](moore_algorithm_1.jpeg)

3. Examine the 8 Neighbors of b0, starting at c0 and going clockwise
4. Let b1 be the first pixel labeled 1, and c1 be the preceding 0.

![](moore_algorithm_2.jpeg)

5. Repeat the process of updating b and c

![](moore_algorithm_3.jpeg)

6. Continue until arrival starting point AND you start repeating the pattern. b=b0 & next = b1

![] (moore_algorithm_4.jpeg)

8. The ordered list of 'b' is the boundary
9. Collect the chain code

![](moore_algorithm_5.jpeg)

![](moore_algorithm_6.jpeg)

Issues of the chain code. (same shape)
- The starting point change changes the sequence order
- The order of direction can be 90º degrees rotated from the other code.
- So its not invariant to rotation nor translations

To be able to match shapes of different orientations we can 
1. order the chain code so it always start with the minimum magnitude integer.
  (so shift the list until start with 0)
2. Just encode the difference between directions 
  (relative vs absolute) 

![](moore_algorithm_7.jpeg)

```
%matlab
bwtraceboundary
```

Note. Derivative <-> Code invariance

### Polygon fitting algorithm
- instead of following indivual pixels, we want to match pixels with a parametrized line
- Convert from RGB to vector image

First Approach: Connect the dots

![](polygon_fitting.jpeg)
