# Lecture 9: Unitary Image Transforms

### General Image transformations
- In 2D a rotation is like a change of basis of the coordinate system

![](rotation_basis.jpeg)

Unitary Transform

![](unitary_transformation.jpeg)

Fourier Transform
- Fourier coeficients for an image
- 90% more energetic coefficients in red
 
![](fourier_transformation.jpeg)

![](2D_fourier_transform.jpeg)

![](fourier_basis.jpeg)

Spatial Basis
- Spatial coeficients for an image
- 90% more energetic coefficient in red

![](spatial_basis.jpeg)

![](2D_spatial_basis.jpeg)

![](spatial_basis.jpeg)

Compression & Parseval Theorem
- You can choose the coefficients who describe the 90% of the image energy

![](parseval_theorem.jpeg)

Different Basis distribute different the energy.
- Pros cons DFT
- Impusle response has infinite coeficients. 
  - A very Localized point, require infinite frequencies to describe it

![pros_cons_dft.jpeg]

![](impulse_response_1.jpeg)
![](impulse_response_2.jpeg)



### Discrete Cosine Transform
- Critical part of the Jpeg algorithm

![](cosine_transform.jpeg)

![](cosine_transform_2.jpeg)

![](jpeg_algorithm.jpeg)

### Discrete Sine Transform

![](sine_transform.jpeg)

### Hadamart Transform
- Doesn't require to compute trigonometric functions
- Recursive definition

![](hadamart_transform.jpeg)

![](hadamart_transform_2.jpeg)

### Haar Transform
- The simpler Wavelet Transform
- Has more local property
- Has a recursive pattern

![](haar_transform_1.jpeg)

![](haar_transform_2.jpeg)


### Wavelet Transforms
- Unitary
- Can Represent Both smooth and discontinuous images without using lots of coefficients
- Local Basis functions
- Computationaly Efficient

![](wavelet_transform.jpeg)

There are wavelet transform algorithms jpeg2000
- .jp2
- .j2c

A mixture between time and Frequency
- Resolution in time vs resolution in freq
- High frequency more localized

![](time_frequency_resolution.jpeg)


Wavelets as filter banks
- wavelet filter bank

![](wavelet_filter_banks.jpeg)

Multiscale/Multiresolution analysis
- Represent what's important at different levels of the image
- Many resolution at different scales

