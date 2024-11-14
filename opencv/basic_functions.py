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
    # sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

    # laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

    # canny
canny = cv.Canny(gray, 150, 175)


# contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours)

# reshaping
dilated = cv.dilate(canny, (7,7), iterations=3)
eroded = cv.erode(dilated, (7,7), iterations=3)
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cropped = img[50:200, 200:400]

# transformation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    # shape[1] = width | shape[0] = height
    return cv.warpAffine(img, transMat, dimensions)
    # -x --> Left
    # -y --> Up
    # x --> Right
    # y --> Down

def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

translated = translate(img, -100, 100)
rotated = rotate(img, -45)
flip = cv.flip(img, -1)


#shapes
blank = np.zeros((500,500,3), dtype='uint8')
blank[200:300, 300:400] = 0,0,255
rect = cv.rectangle(blank.copy(), (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
circle = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
line = cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.putText(blank, 'Hello, world!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

# thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)

# bitwise operations
bitwise_and = cv.bitwise_and(rectangle, circle)
bitwise_or = cv.bitwise_or(rectangle, circle)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
bitwise_not = cv.bitwise_not(circle)

cv.waitKey(1000)
