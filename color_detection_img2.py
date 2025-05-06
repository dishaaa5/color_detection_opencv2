import cv2
import numpy as np

#loading the image
img = cv2.imread(r'c:\Users\Dell\Downloads\colordetetcionimg2.webp')

#resizing the image
img = cv2.resize(img , (500 , 500))

#converting the bgr img to hsv img
hsv_img = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

#Blue Color Detection
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])
blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
blue_result = cv2.bitwise_and(img, img, mask=blue_mask)

#Red Color Detection in both regions
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)
red_result = cv2.bitwise_and(img, img, mask=red_mask)

#Green Color Detection
lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])
green_mask = cv2.inRange(hsv_img, lower_green, upper_green)
green_result = cv2.bitwise_and(img, img, mask=green_mask)

#Yellow Color Detection
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
yellow_mask = cv2.inRange(hsv_img , lower_yellow, upper_yellow)
yellow_result = cv2.bitwise_and(img , img , mask = yellow_mask)

#final output
cv2.imshow("Original Image" , img)
cv2.imshow("Blue Mask", blue_mask)
cv2.imshow("Detected Blue Color", blue_result)
cv2.imshow("Red Mask", red_mask)
cv2.imshow("Detected Red Color", red_result)
cv2.imshow("Green Mask", green_mask)
cv2.imshow("Detected Green Color", green_result)
cv2.imshow("Yellow Mask", yellow_mask)
cv2.imshow("Detected Yellow Color", yellow_result)


cv2.waitKey(0)
cv2.destroyAllWindows()
