import numpy as np
import time
import matplotlib.pyplot as plt
import cv2


#rozmezi barev puku v hsv
low = np.array([90, 86, 1])
high = np.array([192,255,255])



#camera setup
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(3,960) # sirka px
cap.set(4,640) # vyska px



#udela fotku
ret, img = cap.read()



#color masking
pozicepuku = []
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img,low,high)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
if len(contours) != 0:
    for contour in contours:
        if cv2.contourArea(contour) > 10000:
            x,y,w,h = cv2.boundingRect(contour)
            p= x,y,w,h
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),5)
            pozicepuku.append(p)
#plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))


#plt.imshow(cv2.cvtColor(img, cv2.COLOR_HSV2RGB))
i = 0
list_all_x = []
list_all_y = []
for a in pozicepuku:
    x,y,w,h = pozicepuku[i]
    center_x = (x + w/2)
    list_all_x.append(center_x)
    center_y = (y + h/2)
    list_all_y.append(center_y)
    print(center_x, center_y)
    i = i + 1





#toto ukaze fotku
cv2.imshow('image', cv2.cvtColor(img, cv2.COLOR_HSV2BGR))
#odejdu b
cv2.waitKey(0) == ord('b')
cv2.destroyAllWindows()

