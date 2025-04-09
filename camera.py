import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(3,960) # sirka px
cap.set(4,640) # vyska px
#udela fotku
ret, image = cap.read()

#toto ukaze fotku
cv2.imshow('image', image)
#odejdu b
cv2.waitKey(0) == ord('b')
cv2.destroyAllWindows()