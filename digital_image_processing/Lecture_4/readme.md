## Lecture 4: Point operations

### Histograms & Point Operations

Ways to change the image considering the histogram
- Many images with the same histogram. Its not a one-to-one mapping
 
![](histogram_def.jpeg)

```
img = rgb2gray(img)
imhist(img)
```
![](hist_one_to_one.jpeg)

### Point operations
A point transformation of the function, affect every pixel with the same grayscale value in the same way
- Don't change the locations of the pixels
- But redefine its intenisty

![](point_operations.jpeg)

1. Threshold, helps you find bright spots

![](thresholding.jpeg)

2. Digital Negative

![](digital_negative.jpeg)

3. Contrast Stretching
- A darker image can be enhance via linearly stretching its values
- You are not changing the image information (specially if you use a mask), you are showing them differenty
![](contrast_stetretching.jpeg)

![](enhance_contrast.jpeg)

4. Histogram Equalization
- Sometimes, the linear mapping is not enought, different parts of the picture may require different stretching.
- think of an image histogram as a probability mass function
- Or better compute de cumulative density function

![](non_linear_histogram.jpeg)

![](histogram_equalization)

How to transform the original image to a flat uniform distribution?

![](histogram_prob.jpeg)

![](histogram_cdf.jpeg)

![](histogram_uniform.jpeg)

![](histogram_uniform_2.jpeg)

```
histeq
```

5. Histogram Specification
- you can map the histogram into any particular function

![](histogram_specification.jpeg)


6. Gamma Correction
- Every display, has diferernt nonlinear relation between pixels input intensity and display output intensity.
- What i see on my screen is different from my projector.
- Ideally i want a linear relation from what i input to the screen vs what the screen actually shows
- If you konw the gamma of your device, you can compensate the correction

![](gamma_correction.jpeg)

![](gamma_correction_2.jpeg)

![](gamma_correction_3.jpeg)

### Local operations
- Many image operations are locally

Spatial Filter
1. AVG filter
- filter an image by the average of its neighbors
- Helps you smooth noise
        
![](avg_filter.jpeg)

![](conv_filter.jpeg)

2. Edge detecting Filter

![](edge_detector_1.jpeg)

![](edge_detector_2.jpeg)

![](edge_detector_3.jpeg)

# So far
so far we are changing the pixel intensity of the pixels
Next we will apply spatial transformations, as rotating, scaling...
