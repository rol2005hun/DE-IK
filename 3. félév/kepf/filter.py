import cv2
import numpy

#kep beolvasasa
I_origin = cv2.imread("C:/Users/student/Downloads/kacsa.jpg",1)
I_origin = cv2.resize(I_origin,dsize=(0,0),fx=0.75,fy=0.75)

cv2.imshow("eredeti", I_origin)

#Box filter
value = 7 #always odd
I_box = cv2.boxFilter(I_origin, -1, (value, value))

cv2.imshow("box",I_box)


#Gauss filter
sigma_value = 1.05
I_gauss = cv2.GaussianBlur(I_origin, (value, value),sigma_value)
cv2.imshow("gauss",I_gauss)

I_median = cv2.medianBlur(I_origin, value)
cv2.imshow("median",I_median)


#élesítés

I_unsharped = cv2.addWeighted(I_origin, 1.5, I_gauss, -0.5, 0)
cv2.imshow("unsharp",I_unsharped)
cv2.waitKey()