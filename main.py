import pyautogui as pag

import cv2
import numpy as np

startCanvas = (909, 339)
endCanvas = (1447, 633)

canvasWidth = endCanvas[0] - startCanvas[0]
canvasHeight = endCanvas[1] - startCanvas[1]

pen = (1500, 390)
pen = (1500, 390)

column1 = 815
column2 = 840
column3 = 867

row1 = 388
row2 = 418
row3 = 444
row4 = 472
row5 = 501
row6 = 531

black = (column1, row1)
gray = (column2, row1)
blue = (column3, row1)
white = (column1, row2)
clearGray = (column2, row2)
clearBlue = (column3, row2)
green = (column1, row3)
darkRed = (column2, row3)
brown = (column3, row3)
clearGreen = (column1, row4)
red = (column2, row4)
orange = (column3, row4)
clearBrown = (column1, row5)
darkPurple = (column2, row5)
pink = (column3, row5)
yellow = (column1, row6)
purple = (column2, row6)
clearPink = (column3, row6)

img = cv2.imread("img.jpg", -1)
img = cv2.resize(img, (canvasWidth, canvasHeight))

print(canvasWidth, canvasHeight)

#for row in range (img.shape[0]):
#    for column in range (img.shape[1]):
#        print(img[row][column])


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()