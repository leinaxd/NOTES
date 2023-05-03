**NOTES of the Digital Image Processing course by Ruch Radke**

Source:
  Rich Radke Youtube channel:
  https://www.youtube.com/watch?v=UhDlL-tLT2U&list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX
  
  
  
## Lecture 1. Introduction

What is a digital Image?

![camera](origin_of_image.png)

Image Sources:
- Gamma Ray Imaging (High Energy)
    Patient get injected some sort of isotope, the gamma rays get detected by a detector
    - Medical, Cargo

![medical_example_1](medical_example_1.png)
![medical_example_2](medical_example_2.png)
![cargo_example_3](cargo_example_3.png)

- X-Ray (low energy)
    - Mendical, Cargo

![x-ray](x_ray_example.png)
![X-ray2](x_ray_example_2.png)

- Computer Tomography

![](Computational_tomography.png)

- Ultraviolet Imaging
  Sample with a fluorescent dye
- Measuring densities

![](UV-die.png)
![](uv_example_1.png)
![](uv_example_2.png)
![](uv_example_3.png)

Visible-Band Energy:
- Smartphones
- Light Microscope
- Satelite Imaging
- Infra Red (How hot something is)
- Manufacturing / Industrial inspection
- License plate recognition
- Biometrics
- Spacecraft Imaging
  
![sat](satellite_example.png)
![thermal](thermal_image.jpeg)
![mauf](manufacturing_line.jpeg)
![license](license_plate_recognition.jpeg)
![bio](biometrics.jpg)

Micro-wave / Milimiter-wave (THz):
- Radar Image (RPI)
     
![](microwave.jpeg)
![](microwave_example.jpeg)

Radio-wave:
- MRI Magnetic Resonance Imaging (detail)
- Functional MRI (can detect certain proteins)

![](MRI.jpeg)
![](MRI_example.jpeg)
![](fMRI.jpeg)

Non-photon-related imaging:
- Ultrasonic
- Electron Microscope (throwing electrons)
    
![](ultrasonic.jpeg)
![](ultrasound_example.jpeg)
![](electron_microscope.jpeg)

Synthetic Images
- Polution Map / weather map

![](polution_map.jpeg)




## Types of Image Processing


### Low-Level Image Processing

- Preprocessing to 
    - remove Noise
    - Sharpen images
    - Enhance

    INPUT: IMAGE
    
    OUTPUT; IMAGE
 ### Mid-Level Image Processing
 
 - Segmenting an image into Regions/Objects describing an image
    - Diferenciate Cells

    INPUT: IMAGE
    
    OUTPUT: Attributes (edges, lines, regions)



 ### High-Level Image Processing
 
- Making sense of an image
- Understanding
- Computer Vision
- Object Recognition / Face Recognition

    INPUT: IMAGE
    
    OUTPUT: TASK
    
![](original_image.jpeg)
![](low_level.jpeg)
![](mid_level.jpeg)
![](high_level.jpeg)


### Major Acquisition

- How Humans Brain & Eye & visual system works
- How do we represent image & color
- Biology
- How does Camaras adquire
- Cascade

### Image Manipulations & Enhancements

How to maje images betters to me
- Subjective Process like Photoshop
- Rotations 
- Brightness

### Image Restoration

How Much an image was alterated?
Can we undo the process?
- If we know an image has been blured, can we estimate how much?
- Near filter, Estimation filter

### Image Reconstruction from projections

### Image Compression

- Lossless formats (raw)
- Lossy formats (Jpeg)

### Image Segmentation

- Edges, Lines, Objects
- Detecting Primitives

### Image Understanding & Computer Vision

- Object Recognition

### Advanced Topics

- How do you compose objects
- A movie is a compositions of many objects
- Image Watermarking
- Visual Effects
