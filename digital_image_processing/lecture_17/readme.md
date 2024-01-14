```
Author: Eichenbaum Daniel
Email: eichenbaum.daniel@gmail.com
```
This is a practical demo to understand the theory behind:
```
DIP Lecture 14: Object and feature detection ¬Rich Radke
  https://www.youtube.com/watch?v=ddXvs1Wp95A&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX&index=17

Textbook: Sections 12.1-12.2 of Digital Image Processing
  Gonzalez and Woods, 3th ed.  
  https://www.amazon.com/-/es/Rafael-Gonzalez/dp/0133356728  
```

# Lecture 17: Object and Feature Detection
Up to this point we talk about how to get primitives
- Lines
- Use Sobel Edge detector to find edgy points
- And use Hough transform to connect those edgy points with straight lines
- How to use morphological image processing
- How to use Binary image processing to find those points or lines around the boundary

But how do i detect specific objects in the image?
- if i want to detect faces or chairs
- How to go from the low level stuff to higher levels
- Today we will overview how those kind of processes work


EDGES -> LINES -> BOUNDARIES

## Basic Template Matching
Idea. try to slide a template into an image to find where there is a high probability match
- Where the fundamental concept is spatial filtering, like sobel filter
- Same as convolution or correlation
 
![](1_template_matching.jpg)

### Correlation between a template and an image
Think about the image, and the Image as Random Variables.
![](2_template_matching.jpg)

Let $\bar{W(x,y)}$ the avg value of the template
Let $\bar{I_{XY}}$ the avg value of the image inside that window

![](3_template_matching.jpg)

If the $\gamma$ correlation is $+1$ then the template matches perfectly the window (or its a constant times it)
If the $\gamma$ correlation is $-1$ then the template is the flipped intensities (digital negative)
If the $\gamma$ correlation is $0$ then the template is not close the image

`normxcorr2()'

```
%matlab
function findtemplate(im, temp, th, showtemp)
out = normxcorr2(temp, im);
[m,n] = size(temp);
out = out(m+1:end , n+1:end);
bw = out > th;
r = regionprops(bwlabel(bw));

if nargin > 3
  im(1:m, 1:n) = temp;
end

clf
imshow(im, [])
hold on;
for i = 1:length(r)
  rectangle('position', [r(i).Centroid(1), r(i).Centroid ...])
end
```

![](4_template_matching.jpg)

![](5_template_matching.jpg)

If you allow lower correlation threshold, then you can find similar objects

![](6_template_matching.jpg)

It can perform well with noise, but not that much neither

![](7_template_matching.jpg)

Another example is trying to find all windows

![](8_template_matching.jpg)

Increasing the window size makes no match in the image

![](9_template_matching.jpg)
