**NOTES of the Digital Image Processing course by Rich Radke**

Source:
  Rich Radke Youtube channel:
  https://www.youtube.com/watch?v=UhDlL-tLT2U&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX
  
  UCF CRCV 20 lectures
  https://www.youtube.com/watch?v=715uLCHt4jE

Bibliography:
    - Gonzalez and Woods, 3rd ed
  
## Lecture 1. Introduction

- What is a digital Image?
- Examples of digital images
    - Gamma Rays (Medical/cargo)
    - X-Rays
    - Computer Tomography
    - Ultraviolet Imaging (cells)
    - Visible-band (satellite, biometrics, smartphones)
    - Infra red (Thermical images)
    - Microwave (Radar)
    - Radiowave (MRI, fMRI)
    - Non-photon related (Ultrasonic, Electron beam)
    - Synthetic Images (Polution map)
    
- Types of Image Processing
  - Low-level (Image -> Image)
  - Mid-level (Image -> Features)
  - High-level (Image -> Meaning)
  
## Lecture 2. Human Perception
- How humans perceive color
  - Eye anatomy
  - Optical ilusions
- Some definitions
  - Dynamic Range
  - Sensitivity
  - Brightness
- EM Radiation properties
  - Emited Energy (radiant flux W)
  - Perceived Energy (luminous flux Lumen)
  - Density of Energy (lux)
  - Brightness (cd)
- Color
  - Rods
  - Cones
- Chromaticity Diagram
- Adaptive room color control
- Matlab color ramps

## Lecture 3
- How a camera works
  - depth of field
  - image resolution
  - color quality
- Ilumination model
- Sampling & Quantization
- Distance between images
- Video

## Lecture 4
- Histograms
- Point Operations
  - Threshold
  - Digital Negative
  - Contrast stretching
  - Histogram Equalization
  - Histogram Specification
  - Gamma correction
- Local Operations
  - AvG filter
  - Edge detection filter

## Lecture 5
- Geometric transformations
  - Translation
  - Scaling
  - Flipping
  - Rotation
  - Shearing
- Isometric Transformations
- Affine Transformations
- Automatic Alignament
- Color interpolation

- Projective Transformations


## Lecture 6: Spatial Filters
- 1D filters
- 2D filters
- Low pass filters
  - Avg filter
  - Gaussian Filter
- High Pass filters
  - derivative filter
  - Sobel
- Sharpen
- Unsharpen
- Non linear filters
  - Median filter
  - Salt & Pepper noise

## Lecture 7: 2D- Discrete Fourier Transform
- Definitions
- Basis functions
- DFT of an image
- Shifting the DFT
- Striping lines
- DFT properties

##  Lecture 8: Frequency Domain Filtering, Sampling & Aliasing
- Box mask & circle mask
- Impulse response
- Gaussian Filter
- High Pass filter
- Laplacian Filter
- Sampling & Aliasing
- Antialiasing Filter
- Moire patterns

## Lecture 9: Unitary Image Transforms
- Unitary transform
- Fourier Basis Transform
- Spatial Basis Transform
- Compression & Parseval Theorem
- Limitations DFT
- Discrete Cosine Transform
- Discrete Sine Transform
- Hadamart Transform
- Haar Transform
- Wavelet Transform
- Jpeg / Jpeg2000 algorithm
- Time vs Frequency trade off
- Multiresolution Analysis

## Lecture 10: Edge detection
- Ideal edges
- Real world edges
- Image gradients
- Gradient operators
  - Laplacian
  - Laplacian of a Gaussian
  - Difference of Gaussians
  - Scale-invariant feature transform (SIFT) for object detection
- Canny Edge detector

## Lecture 11: Edge linking and line detection
- Moore's Boundary Following Algorithm
  - Sequence Chain code
- Polygon Fitting Algorithm
- The Hough Transform
  - (rho, theta) plane
  - Drawing Hough lines
  - Preprocessing before Hough transform
