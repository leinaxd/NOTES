
## Lecture 7: 2D discrete fourier transform
1D fourier transform

![](1D_DFT.jpeg)

2D fourier transform

![](2D_DFT.jpeg)

2D fourier transform is separable
- The first term is the sum of all pixels intensities (makes sense to plot in a logarithmic scale)

![](2D_DFT_2.jpeg)

![](DFT_0_0.jpeg)

Basis functions
- Symetric respect NFFT/2
- High freq at NFFT/2

![](basis_fn_DFT_1.jpeg)

![](basis_fn.jpeg)

DFT of an image
- High frequency = edges
- Low frequency = planes

![](DFT_image.jpeg)

In the shifted version, 
- You can see low frequency strong lines
- Remember DFT, the image is periodically repeated
- you can see that the discontinuity of the borders of the image, implies a delta response in frequency at both axis

![](shifted_DFT.jpeg)

![](repeated_boundaries.jpeg)

In this example you can see a strong diagonal lines

![](DFT_example.jpeg)

In this example, you don't have a missmatch border, and the pattern is kind of circular

![](DFT_example_2.jpeg)


### Fourier transform properties
Note. we didn't talk about phase yet.

Shifting
- You don't change the absolute value but the phase

Scale/Flip
- **Scale Brightness**, scaling the intensity of the image corresponds to scaling the frequency of the image
- **Scale Size**, Scale the size of the image

![](scaling.jpeg)

Rotation

![](rotation.jpeg)

Convolution
- Appling convolution in the time domain is more efficient than in the frequency domain
 
![](convolution.jpeg)

Linear convolution 

![](linear_conv.jpeg)

Circular Convolutio

![](circular_conv.jpeg)

![](circular_conv_2.jpeg)

![](circular_conv_3.jpeg)

![](circular_conv_4.jpeg)

![](circular_conv_5.jpeg)


### Correlation

![](angle_edges.jpeg)

![](angle_edges_2.jpeg)

![](angle_edges_3.jpeg)

![](angle_edges_4.jpeg)

Stripes lines are rotates 90º in frequency domain

![](stripes_angles_explanation.jpeg)

![](stripes_angles_explanation_2.jpeg)
