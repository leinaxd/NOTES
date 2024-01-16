```
Author: Eichenbaum Daniel
Email: eichenbaum.daniel@gmail.com
```
This is a practical demo to understand the theory behind:
```
DIP Lecture 16: Lossy image compression ¬Rich Radke
  https://www.youtube.com/watch?v=wyb5S8QsCSA&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX&index=19

Textbook: Sections 8.2.8 of Digital Image Processing
  Gonzalez and Woods, 3th ed.  
  https://www.amazon.com/-/es/Rafael-Gonzalez/dp/0133356728  
```

# Lecture 19: Lossy Image Compression

The idea behind Lossy compression is that some types of data are less sensitive to little change in values.
- You won't notice if an image had changed a bit
- Jpeg

Block Transform Encoding
- Given an $M\times N$ image
- Break it into $n\times n$ blocks (i.e. n=8,16)
- Apply forward $n\times n$ Transform for each block
- Quantize (round some information)
- Symbol Encoder
- Compressed Image File

Block Transform Decodeing
- Given the compressed image
- Symbol decoder
- Inverse $n\times n$ transform
- Resemble blocks
- Decompressed image

![](1_lossy_transform.jpg)

There's a choise of which 2D transform to choose
- We've seen the DFT, but it has complex values
- Discrete Cosine Transform DCT (jpeg)
  - Has only real values
  - compact energy into low frequency
- wavelet transform is used in jpeg 2000
- Hadamart
- Haar

DCT transform is as follows:
- from 8 x 8 block pixels to 8 x 8 block coefficients
  
![](2_lossy_transform.jpg)

One opportunity for compression is 
- Zonal Coding: How many bits per coeficcient as a function of $(u,v)$
