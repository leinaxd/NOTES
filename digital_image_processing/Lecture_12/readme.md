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
