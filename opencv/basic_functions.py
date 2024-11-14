import cv2 as cv

img = cv.imread("C:\\Users\\rahul\\OneDrive\\Desktop\\python101\\opencv\\resources\\photos\\cat.jpg")
cv.imshow("image", img)

# color_spaces
gray = cv.cvtcolor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtcolor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtcolor(img, cv.COLOR_BGR2LAB)
rgb = cv.cvtcolor(img, cv.COLOR_BGR2RGB)

# blurring
average = cv.blur(img, (3,3))
gauss = cv.GaussianBlur(img, (3, 3), 0)
median = cv.medianBlur(img, 3)
bilateral = cv.bilateralFilter(img, 10, 35, 25)

# Edge Detection


cv.waitKey(1000)
