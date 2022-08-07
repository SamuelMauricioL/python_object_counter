import cv2

# from PIL import Image

IMAGE_PATH = "assets/colors_dot.jpg"
BASE_WIDTH = 100

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
'''
El humbral(threshold) es el rango definido en la escala de grises
    - gray_scale_range_min
    - gray_scale_range_max
este rango es usado para filtrar todos los valores fuera de este rango
e invertir la escala de pixeles aplicando THRESH_BINARY_INV + THRESH_OTSU
'''
gray_scale_range_min = 100
gray_scale_range_max = 255

th, threshed = cv2.threshold(
    resized_image,
    gray_scale_range_min,
    gray_scale_range_max,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,
)

# cv2.imshow("img", threshed)
# cv2.waitKey(0)

# findcontours
contours = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


# filter by area
stride_min = 10
stride_max = 30
contours_detected = []
for contour in contours:
    if stride_min < cv2.contourArea(contour) < stride_max:
        contours_detected.append(contour)

print("\nDots number: {}".format(len(contours_detected)))
