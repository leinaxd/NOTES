```
Author: Eichenbaum Daniel
Email: eichenbaum.daniel@gmail.com
```
This is a practical demo to understand the theory behind:
```
DIP Lecture 23: Photomontage and inpainting ¬Rich Radke
  https://www.youtube.com/watch?v=XTRO6yQOvJc&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX&index=26

Follows Sections 3.3-3.4 of the textbook.  http://cvfxbook.com/

Key references:

A. Agarwala, M. Dontcheva, M. Agrawala, S. Drucker, A. Colburn, B. Curless, D. Salesin, and M. Cohen. Interactive digital photomontage. In  ACM SIGGRAPH (ACM Transactions on Graphics), 2004. 
http://dx.doi.org/10.1145/1015706.101...

M. Bertalmio, G. Sapiro, V. Caselles, and C. Ballester. Image inpainting. In  ACM SIGGRAPH (ACM Transactions on Graphics), 2000. 
http://dx.doi.org/10.1145/344779.344972

A. Criminisi, P. Pérez, and K. Toyama. Region filling and object removal by exemplar-based image inpainting.  IEEE Transactions on Image Processing, 13(9):1200--12, Sept. 2004. 
http://dx.doi.org/10.1109/TIP.2004.83...

```

# Lecture 26: Photomontage and inpainting

Last time we talked abouut image compositing and forensic.

Now we want to find a dividing line to blend both images

![](1_photomontage.jpg)

we are not trying to disguise the dividing line we are calling the 'seam'.

In this occasion we are trying to find the least obtrusive seam possible  


The goal is to find a good seam (dividing line) between 2 images so that intensity differences across the seam is imperceptible
- The idea is to compare the colors of adjacent pixels across the line

![](2_photomontage.jpg)

So the 'COST' of drawing a line between pixels i and j, are the difference:
- ||Pixel of source - Pixel of target|| for each side should be minimized
  
![](3_photomontage.jpg)

Another possible idea is to modify this respect to respect to image gradients
