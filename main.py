import cv2

# from PIL import Image

IMAGE_PATH = "assets/colors_dot.jpg"
BASE_WIDTH = 200

image_gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

### Resize Image
"""
Es necesario hacer un resize de la image deacuerdo al BASE_WITDH
para no afectar los limites de los stride's(s1 && s2) definidos 
"""
height, width = image_gray.shape[:2]
BASE_HEIGHT = int(BASE_WIDTH * height / width)
resized_image = cv2.resize(image_gray, (BASE_WIDTH, BASE_HEIGHT))


th, threshed = cv2.threshold(
    resized_image,
    100,
    255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU,
)

cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

s1 = 3
s2 = 20
xcnts = []
for cnt in cnts:
    if s1 < cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)

# cv2.imshow("img", threshed)
# cv2.waitKey(0)

print("\nDots number: {}".format(len(xcnts)))
