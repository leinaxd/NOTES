Book Robot vision
- Berthold Klaus, Paul Horn

# Lecture 6: Spatial filter


Recall 1-D filter
- 2D filter, odd dimension (symetrical respect origin)

![](1D_filter.jpeg)

![](2D_filter.jpeg)

![](2D_filter_2.jpeg)

Looks almost like correlation
- The only difference is wheather you flip the filter or not.

If filters components adds to 1, then you preserve the original intensity.

Note.
```
Filter2(h, img)
# Gets actual floating point results
#Not scaled to  [0, 255

imFilter(h, img)
#uint8 -> uint8
#works with color
#May loose important values <0 or >255
```


### Low pass Filters
Moving avg
- Repleace each filter via a weighted average of its neighbors
- Pros: Reduces certain kind of noise
- Cons: Blur the image

![](noise_reduction.jpeg)

You can combine, filtering and threshold

![](filtering_threshold.jpeg)

Gaussian Filter
- Adjusting sigma you control the cut-off frequency
- 
![](gaussian_filter.jpeg)

### High pass filter
Instead of looking the sum of pixels (int), take the difference of pixels
- result is sharpening
- can also be combined with threshold for edge detection

```
H_pf = Id - H_lp
```

1D example.
- large slopes, larger derivatives

![](1D_dif.jpeg)
![](1D_dif.jpeg)

![](2D_dif.jpeg)

![](dif_filter_threshold.jpeg)

How to enhance (sharpen)
- cons: you also enhance noise

![](enhance_filter.jpeg)

![](enhance_filter_2.jpeg)

Unsharp masking
- Just add a fraction of the difference edge

![](unsharp_masking.jpeg)

![](unsharp_masking_2.jpeg)

Sobel 
- Filters do not need to be symetric

![](sobel_1.jpeg)

![](sobel_2.jpeg)

### Non Linear filters
Salt & Pepper noise
- Random pixels are set to 0 or 255

![](salt_pepper_noise.jpeg)

Not all image filters are linear

Median Filter

![](median_filter.jpeg)

![](median_filter_2.jpeg)

When to use gaussian, when median?

![](gaussian_median_when.jpeg)

All filters can be applied locally
