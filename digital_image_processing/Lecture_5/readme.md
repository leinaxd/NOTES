

# Geometric operations
- In euclidean transformations

![](geometric_operations.jpeg)


- Translation

![](translation_1.jpeg)
![](translation_2.jpeg)

- Scaling
 
![](scaling.jpeg)
![](scaling_2.jpeg)
![](scaling_3.jpeg)

- Flip

![](flip.jpeg)

- Rotation

![](rotation.jpeg)

- Shear

![](shear_img_1.jpeg)

![](shear_img_2.jpeg)

![](shear_img_3.jpeg)



### Forward Mapping
Similarity transformation
- Scale + Shift + Flip
- Preserves Parallel lines

![](forward_mapping.jpeg)

![](forward_mapping_2.jpeg)

![](forward_mapping_3.jpeg)

Isometric Transformation
- Preserves shapes, angles

![](isometric_transformation.jpeg)

Projective Transformation

![](projective_transformation.jpeg)

### Automatic Alignament
- (dual align is a more robust version)
Align a collection of image to build a bigger picture
1. Find the same points in multiple images.
2. Find the affine transformation for each image
3. Use linear regression to find the best alignments

Version 2
Repeat but with a projective transformation

Version 3
Can you model the lens distortion?

version 4
can the points be found automatically?
```
cpselect(im1, img2) #selects those points in both images

function mosaic(I, J, pt1, pt2):
  S = size(I)
  T = fitgeotrans(pt1, pt2, 'affine)
  Iregistered = imwarp(I, T, 'OutputView', imref2d([s(1), 2*s]))
  Jregistered = imwarp(J, affine2d(eye(3)), 'OutputView', imref2d([s(1), 2*s]))
  
  Imask = any(Iregistered, 3) > 0
  Jmask = any(Jregistered, 3) > 0
  
out = mosaic(im1, im2, movingPoints, fixedPoints)
```
![](corresponding_points.jpeg)

![](inverse_transformation.jpeg)

![](forward_transformation.jpeg)
![](backwards_transformation.jpeg)


### color interpolation
Bilinear Interpolation
- Given 4 fixed points, you want a linear interpolation between 2 pivel values

![](bilinear_interpolation.jpeg)

![](other_interpolation.jpeg)

