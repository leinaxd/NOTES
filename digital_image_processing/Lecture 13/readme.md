```
Author: Eichenbaum Daniel
Email: eichenbaum.daniel@gmail.com
```
This is a practical demo to understand the theory behind:
```
DIP Lecture 12a: Image Segmentation ¬Rich Radke
    https://www.youtube.com/watch?v=ZF-3aORwEc0&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX&index=14

Textbook: 10.4-10.6 Digital Image Processing
  Gonzalez and Woods, 4th ed.  
  https://www.amazon.com/-/es/Rafael-Gonzalez/dp/0133356728  
```

# Lecture 13: Image segmentation

Introduction
  - Basic Region Growing
  If you threshold the whole image, what you may get is a disconnected regions that are above the threshold.
  You can clean some of this stuff with what its called "morphological image processing" where you can select the region you care so on.
  
  ![](regions.jpg)

  Basic algorithm to shrink each region to one point.

  1. From input image I(x,y), get a **Binary "Seed Image"** $S(x,y)S for locations of interest. (e.g. thresholding)
  There're ways to shrink them automatically.
    ![](regions_shrinked.jpg)
  2. Reduce the seed image down to a single point (centroid) each blob of the seed. (e.g. erosion)
  3. Let new image $T(x,y)=1\ if\ I(x,y)\ satisfies some predicate$.
     e.g. all points connected to a given seed point $(x_i, y_i)$ and $|I(x,y) - I(x_i, y_i)|\le T$.

     For example given a point, find all intensities closer to that value.
      - keep growing the contour.
     ![](contour_growing.jpg)

    ` matlab: grayconnected `
    
![](grayconnected.jpg)
