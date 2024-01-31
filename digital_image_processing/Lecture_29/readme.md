```
Author: Eichenbaum Daniel
Email: eichenbaum.daniel@gmail.com
```
This is a practical demo to understand the theory behind:

```
DIP Lecture 25: Active shape models ¬Rich Radke
  https://www.youtube.com/watch?v=53kx_czs7Es&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX&index=29

Key references:

T.F. Cootes, C.J. Taylor, D.H. Cooper, J. Graham
Active Shape Models - Their Training and Application
http://dx.doi.org/10.1006/cviu.1995.1004
```

# Lecture 29: Active Shape Models

The topic of today is a computer vision problem called 'active shape models'
- So far we've studied the low level of images, computing gradients, connecting edges into lines
- We didn't understood what's really going on in the image
- This lecture is about image understanding or computer vision.

Active Shape Models is a different type of object detection.
- for example, licence plate detection.
- Not template based.


Template base object runs a patch over the image.
- For example a plate over the car image.

![](1_vision.jpg)

That work pretty well for rigid object (they don't change in size)


If you are searching for faces instead, many people have different face features. 
- So this will be usefull for not rigid shapes.

![](2_vision.jpg)

For this to work i need to collect many faces.
- i need to manually assign points to define the face.
- we are trying to find common locations that i can put into correspondance 
 
![](3_vision)


IDEA:
- Given an image and a mask
- Using a convlutional neural net to search the car plate over the image,
- The mask is telling you the right object position. The true target.
- The task of the neural net is to predict a binary mask for the location of the plate.


![](4_vision.jpg)


### Procrustes Analysis
Greek myth, he was a bandit, he would tie his victims to an iron bed and he would chop off their limbs or stretch them so they fit to bed.
- Scale and stretch

The first thing to do is to scale, rotate and translate each set of points. 
- So the first problem is alignment

Algorithm 1
1. Translate all shapes to be centered at (0,0)
2. Now take one of the shapes $Z^1$, and we are going to scale it, so it has length 1 $||Z^1|| = 1$
3. Scale and rotate everything else (all other shapes) to align with this shape

For each person $a^i$ i'm going to compute the vector for person j and the vector for peson 1.

![](5_vision.jpg)

Then do some manipulations between the X and Y coordinate for person 'j' respect to person 'i'

![](6_vision.jpg)

The magic formula is 
- This is telling me how to scale and rotate person 'j' to align to person number 1
  
![](7_vision.jpg)


My new values for person 'j' will be scale and rotate.


![](8_vision.jpg)


So now, we have $S$ sets of aligned Training sets.

Each of them is described by a 2n-vector of feature points.


Clearly these 2n points are not all independant
