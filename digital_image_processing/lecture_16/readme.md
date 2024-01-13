```
Author: Eichenbaum Daniel
Email: eichenbaum.daniel@gmail.com
```
This is a practical demo to understand the theory behind:
```
DIP Lecture 13a: Region Description and filtering ¬Rich Radke
  https://www.youtube.com/watch?v=_kwZj-EB1OU&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX&index=16

Textbook: Sections 12.1-12.4 of Digital Image Processing
  Gonzalez and Woods, 3th ed.  
  https://www.amazon.com/-/es/Rafael-Gonzalez/dp/0133356728  
```

# Lecture 16: Boundary, Region Description and Filtering

So far we talked about Finding shapes like Graph cutting, active contours or just playing with thresholding
- They were focused on finding a single shape that we called 'foreground' and trying to separate from the 'background'
- We also talked about Erosion, Dilation, opening, closing to get rid of undesirables objects
- A real life example involves the finding of many shapes like in a petri dish

![](petri_dish.jpg)

We will talk about
- Shape of objects
- Texture of objects
- matlab 'regionprops' (properties of an object)

## SHAPE PROCESSING

![](blob_properties.jpg)

- Perimeter
- Area
- Diameter (the longest path between two points that are on the boundary)
- Bounding Box (smallest rectangle enclosing the object)

Compactness of the blob
- The smallest you can do is a circle
- With the same Area you can increase the perimeter

![](compactness.jpg)
![](circularity)

Centroid or Center of mass.
- Where are most of the pixels locates. (avg of all points)

![](centroid.jpg)

What is the best fit ellipse?
- How to fit the best ellipse in the object
- Eigenvalues and Eigenvectors tell us the size and orientation of the ellipse

![](ellipse_fit.jpg)

![](eigenval.jpg)
