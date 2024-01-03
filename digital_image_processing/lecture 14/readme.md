```
Author: Eichenbaum Daniel
Email: eichenbaum.daniel@gmail.com
```
This is a practical demo to understand the theory behind:
```
DIP Lecture 12b: Snakes, Active Contours and level sets ¬Rich Radke
    https://www.youtube.com/watch?v=RJEMDkhVgqQ&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX&index=14

Textbook: ch. 11 Digital Image Processing
  Gonzalez and Woods, 4th ed.  
  https://www.amazon.com/-/es/Rafael-Gonzalez/dp/0133356728  
```

# Lecture 14: Image segmentation continuation

Instead of dealing with Pixel level segmentation, we are about to deal with curved level segmentation.
- The idea is to segment curves, not pixels.
- The convex hull evolves shrinking like a rubber band

![](active_contour_1.jpg)
![](active_contour_2.jpg)


Its an iterative process, we want a segmentation curve that.
1) Conforms to Image Edges
2) Is a smoothly varying curve vs lots of jagged rooks and crannies Tradeoff

What is a good curve? Define a cost function.


