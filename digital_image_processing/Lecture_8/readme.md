Books:
  Gonzalez and Woods, Sections 4.7-4.9, 4.11

# Frequency domain filtering, sampling and Aliasing 

Pipeline
- Spatian Domain convolution <-> Frequency Domain Multiplication

![](filtering_pipeling.jpeg)


### Box mask & Circle mask

![](masks.jpeg)

### Impulse response
- Smaller the cutoff freq => more blurring & bigger the ringing
- The solution is a smoother filter design 

![](impulse_response_1.jpeg)

![](impulse_response_2.jpeg)

![](ringing.jpeg)


### Gaussian filter
- Is good at time domain as well as frequency domain
- You can smooth the image without the ringing artifact 

![](gaussian_filter_1.jpeg)

![](gaussian_filter_2.jpeg)

### High pass filter

![](high_pass_filter.jpeg)

![](high_pass_filter_2.jpeg)

### Laplacian filter
- Laplacian's filter represents the second derivatives of the image for both directions aka laplacian
- Also you can combine a low pass Gaussian filter with a high pass laplacian, achieving a band-pass filter

![](laplacian_filter.jpeg)
![](laplacian_2.jpeg)


### Sampling & Aliasing

![](sampling.jpeg)

You have to sample at least 2ble nyquist frequency, otherwise if you want to sample a chessboard you will end up sampling a black image

![](sampling.jpeg)

Antialiasing filter

![](antialiasing.jpeg)

![](antialiasing_2.jpeg)

![](sampling_2.jpeg)

The Woman on the right was downsampled by 4

![](sampling_3.jpeg)

You can apply an antialiasing filter, but you are loosing the detail
- However you can downsampling it now without problems
 
![](sampling_4.jpeg)

In video games, you want to have a good render for text.
- The idea here is to upsample the image by 4, then apply some blundering techinique

![](antialiasing_3.jpeg)


Moire patterns
- 2 images with different frequency, any rotation doesn't change the frequency.
- maybe an aliasing of our vision

![](moire_1.jpeg)

![](moire_2.jpeg)
