import cv2 as cv
import numpy as np
import glob
import imutils

image_paths = glob.glob("C:\\Users\\rahul\\OneDrive\\Desktop\\python101\\opencv\\resources\\stitching\\*.jpg")
images = []

for image in image_paths:
    img = cv.imread(image)
    images.append(img)
    cv.imshow("Image", img)
    cv.waitKey(0)

# it will take some time
imgStitcher = cv.Stitcher_create()
error, stitched_img = imgStitcher.stitch(images)

if not error:
    # cv.imwrite("stitchedImage.png", stitched_img)
    cv.imshow("stitchedImage", stitched_img)
    cv.waitKey(0)
