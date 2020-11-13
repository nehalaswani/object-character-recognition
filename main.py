import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\dell\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('image.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

#Detecting Words
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
print(boxes)
boxes = pytesseract.image_to_data(img)
for a,b in enumerate(boxes.splitlines()):
        #print(b)
        if a!=0:
            b = b.split()
            if len(b)==12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 1)

cv2.imshow("Result",img)
cv2.waitKey(0)
