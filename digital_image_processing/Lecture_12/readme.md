# Lecture 12: Thresholding
- Image segmentation
- How to separate foregroud from background


![](image_segmentation_1.jpeg)

If the foreground is dark you can threshold it

![](image_segmentation_2.jpeg)

If the background image has a different brightness from the foreground you can threshold from histogram

![](image_segmentation_3.jpeg)

How to automatically select the threshold.
How to automatically fill the holes in the foreground (morphological image processing)

The idea is to separate / classify the brightness into 2 groups
- The quality of the processing relies on the quality of the histogram

- ![](image_segmentation_4.jpeg)

![](thresholding.jpeg)

![](thresholding_2.jpeg)

So this is an argument for local thresholding.

Global Thresholding
- Assume you are using the same threshold T for the whole image.
- How to find the best threshold?

Otsu's algorithm
- Split the image of the image into 2 classes
- Choose a threshold, that makes those classes the most separated as possible
Maximize the between-class variance
- A good threshold should separate pixels into tight clusters

![](global_statistics.jpeg)

Those pixels above/below the threshold

![](global_statistics_2.jpeg)

Probability of each class

![](global_statistics_3.jpeg)

Mean and variance for each class

![](global_statistics_4.jpeg)

Otsu's criterion is to maximize the between class variance:

![](global_statistics_5.jpeg)

So look at the ratio of variance as a measure of separability
- Higher ratio means more separable

![](global_statistics_6.jpeg)

In practice we just consider all possible K and choose T as the k that maximizes variance

![](global_statistics_7.jpeg)

```
%matlab
graythresh
```

Original Image:

![](otsu_method_1.jpeg)

Background mask

![](otsu_method_2.jpeg)

Histogram 

![](otsu_method_3.jpeg)

Cost Function
- The circle shows the threshold value

good for text images

![](otsu_method_4.jpeg)
![](otsu_method_4.jpeg)

This algorithm can be extended for finding K-1 Classes
- The implementation is more tricky as you only can separate 2 classes and iterate
- Or using numerical optimization

![](global_statistics_8.jpeg)

Otsu can fail when there's no strong pixel in the histogram
- like the circle in the iluminated background
- Or if the object is small respect the background

![](otsu_method_7.jpeg)

Remedies:
- Low pass filter, then apply otsu
- Only consider pixels near edges when computing the threshold (draw a boundary)

![](otsu_method_8.jpeg)

# Adaptive Threshold
Blockproc
- Apply a specified function to each MxN Block
1. Split image into blocks
2. Find the threshold locally to each block

```
blockproc(img, [M,N], func)
```

![](blockproc.jpeg)

it apears some artefact (edges of blocks)
- Blocksize is tricky

Another approach is to get away of the blocks
- Adapt threshold for each pixel
- At each pixel build a neighborhood, compute mean and variance

![](blockproc_2.jpeg)

Apply a decision rule to each block

![](blockproc_3.jpeg)

Can also be applied to different channels

![](blockproc_4.jpeg)

If applied with multiple clusters you can apply machine learning methods

![](blockproc_5.jpeg)
