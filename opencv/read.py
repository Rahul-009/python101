import cv2 as cv

img = cv.imread("C:\\Users\\rahul\\OneDrive\\Desktop\\python101\\opencv\\resources\\photos\\cat.jpg")
cv.imshow("image", img)
cv.waitKey(1000)

capture = cv.VideoCapture("C:\\Users\\rahul\\OneDrive\\Desktop\\python101\\opencv\\resources\\videos\\kitten.mp4")

while True:
    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow("video", frame)
        if cv.waitKey(20) & 0xFF==ord('q'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
