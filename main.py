import cv2

# from PIL import Image

IMAGE_PATH = "assets/colors_dot.jpg"
BASE_WIDTH = 200

image_gray = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

### Resize Image
"""
Es necesario hacer un resize de la image deacuerdo al BASE_WITDH
para no afectar los limites de los stride's(stride_min && stride_max) definidos 
"""
height, width = image_gray.shape[:2]
BASE_HEIGHT = int(BASE_WIDTH * height / width)
resized_image = cv2.resize(image_gray, (BASE_WIDTH, BASE_HEIGHT))

# threshold
gray_scale_range_min = 100
gray_scale_range_max = 255

th, threshed = cv2.threshold(
    resized_image,
    gray_scale_range_min,
    gray_scale_range_max,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU,
)

# findcontours
contours = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


# filter by area
stride_min = 3
stride_max = 20
xcnts = []
for contour in contours:
    if stride_min < cv2.contourArea(contour) < stride_max:
        xcnts.append(contour)

# cv2.imshow("img", threshed)
# cv2.waitKey(0)

print("\nDots number: {}".format(len(xcnts)))
