from Stitcher import Stitcher
import cv2 as cv

imageA = cv.imread('2.jpg')
imageB = cv.imread('1.jpg')

sticher = Stitcher()
(result, vis) = sticher.stitch([imageA, imageB], showMatches=True)

cv.imshow('imageA', imageA)
cv.imshow('imageB', imageB)
cv.imshow('vis', vis)
cv.imshow('result', result)
cv.waitKey(0)
cv.destroyAllWindows()
