import cv2

imagePath = "assets/black_dot.jpg"

gray = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

th, threshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

s1 = 30
s2 = 60
xcnts = []
for cnt in cnts:
    if s1 < cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)

cv2.imshow("img", threshed)
cv2.waitKey(0)

print("\nDots number: {}".format(len(xcnts)))
