```
Author: Eichenbaum Daniel
Email: eichenbaum.daniel@gmail.com
```
This is a practical demo to understand the theory behind:
```
DIP Lecture 13: Morphological image processing ¬Rich Radke
  https://www.youtube.com/watch?v=IcBzsP-fvPo&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX&index=15

Textbook: Sections 9.1-9.5 of Digital Image Processing
  Gonzalez and Woods, 3th ed.  
  https://www.amazon.com/-/es/Rafael-Gonzalez/dp/0133356728  
```

# Lecture 15: Morphological Image Processing

We want to operate in a binary image. (i.e. after thresholding)

There might be some pixels that should be black and other ones that should be white.

![](binary_image.jpg)

![](binary_image_2.jpg)
![](binary_image_3.jpg)



Morpho = shape based processing.

Morphological operators takes a **set of pixels** and returns a **set of pixels**

Key Element "**Structure element**" is a small template that helps produce the new image from the old one.




