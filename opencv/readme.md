# Open source computer vision library

## Blurring Techniques

blurring used to reduce noise and smoothing

- Average Blur  
  doesn’t preserve edges well.
- Gaussian Blur  
  Applies a Gaussian function (bell curve) to the kernel, giving more weight to the central pixels, resulting in smoother blur and better preservation of edges compared to averaging.
- Mean Blur  
  Effective for images with noise, especially impulse noise
- Bilateral Blur  
  Unlike other blurring techniques, bilateral filtering smoothens the image while preserving edges by considering both spatial and intensity differences.
  Useful for edge-preserving smoothing in applications like portrait retouching and cartoon effects.

## Edge Detection

- Sobel
  compute the gradient of the image intensity at each pixel, detecting edges based on changes in intensity.  
  Calculates derivatives in the x and y directions (using separate kernels) and combines them to detect edges.

used when direction-specific edge detection is needed.

- scharr  
  A variant of Sobel with improved accuracy for smaller kernel sizes

- Laplacian  
  detects edges by calculating the second derivative in all directions, which captures areas of rapid intensity change.  
   it can detect edges in all directions, but it’s sensitive to noise.

- Canny
  A multi-step algorithm that combines gradient calculation, non-maximum suppression, and edge tracking using double thresholds to produce strong, accurate edges.

## thresholding

Thresholding is a technique in OpenCV (and image processing in general) to create a binary image from a grayscale image. It converts pixel values to either 0 (black) or 255 (white), based on a threshold value. This process is widely used in object detection, image segmentation, and feature extraction.

- adaptive  
  Adaptive thresholding is useful when there is uneven lighting in an image. It calculates the threshold for small regions, making it more flexible for varying illumination conditions.

## Image Stitching steps

- image loading
- overlapping feature detection and matching
- homography(transformation) calculation. (scale, rotate, translate) RANSAC algorithm\*
- warp image to align them
- blend the warped images smoothly to reduce visible seams and brightness differences

## python vs cpp vs cython

python actually runs cpp code behind the scene  
it is slow. the complexity stacks and become headache for large projects

That's why for large and real time project cpp/cython is better
