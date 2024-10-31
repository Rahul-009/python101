# pip install opencv-python
import numpy as np
import cv2 as cv
import glob
import os


#def calibrate(showPics = True):
    #read image
root = os.getcwd()
calibrationDir = os.path.join(root, 'opencv\\resources\\chessboard')  # windows path
imgList = glob.glob(os.path.join(calibrationDir, '*.jfif'))

# initialize
nRows = 9
nCols = 6
termCriteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

worldPtsCur = np.zeros((nRows*nCols, 3), np.float32)
worldPtsCur[:, :2] = np.mgrid[0:nRows, 0:nCols].T.reshape(-1, 2)  

worldPoints = []
imgPoints = []
showPics = True

# Find corners
for curImgPath in imgList:
    imgBGR = cv.imread(curImgPath)
    imgGray = cv.cvtColor(imgBGR, cv.COLOR_BGR2GRAY)
    cornersFound, cornersOrg = cv.findChessboardCorners(imgGray, (nRows, nCols), None)

    if cornersFound == True:
        worldPoints.append(worldPtsCur)
        cornersRefined = cv.cornerSubPix(imgGray, cornersOrg, (11, 11), (-1, -1), termCriteria)
        imgPoints.append(cornersRefined)
        if showPics:
            cv.drawChessboardCorners(imgBGR, (nRows, nCols), cornersRefined, cornersFound)
            cv.imshow('Chessboard', imgBGR)
            cv.waitKey(500)

cv.destroyAllWindows()

# calibrate
repError, camMatrix, distCoeff, rvecs, tvecs = cv.calibrateCamera(worldPoints, imgPoints, imgGray.shape[::-1], None, None)
print('Camera Matrix:\n', camMatrix)
print('Reproj Error (pixels): {:.4f}'.format(repError))

# saveCalibration
curFolder = os.path.dirname(os.path.abspath(__file__))
paramPath = os.path.join(curFolder, 'calibration.npz')
np.savez(paramPath, 
    repError = repError,
    camMatrix = camMatrix,
    distCoeff = distCoeff,
    rvecs = rvecs,
    tvecs = tvecs
    )
