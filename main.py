import cv2

imagePath ="assets/black_dot.jpg"


gray = cv2.imread(imagePath, 0)

th, threshed = cv2.threshold(gray, 100, 255,
       cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

cnts = cv2.findContours(threshed, cv2.RETR_LIST,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]

s1 = 3
s2 = 20
xcnts = []
for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
        xcnts.append(cnt)


print("\nDots number: {}".format(len(xcnts)))