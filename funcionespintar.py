import cv2 as cv
import numpy as np


img = np.ones((500,500,3), np.uint8)*150

#cv.rectangle(img,(10,10), (200,200), (34,56,100),-1)
cv.line(img, (400,255), (450,250), (0,165,255),50)
cv.line(img, (240,255), (240,480), (0,165,255),25)
cv.line(img, (170,270), (170,480), (0,165,255),25)
cv.line(img, (170,480), (190,480), (0,165,255),25)
cv.line(img, (240,480), (260,480), (0,165,255),25)
cv.circle(img,(305,255),100,(0,255,255),-1)
cv.circle(img,(200,350),100,(0,255,255),-1)
cv.circle(img,(340,250),40,(255,255,255),-1)
cv.circle(img,(340,250),10,(0,0,0),-1)

cv.imshow('img',img)
cv.waitKey(0)