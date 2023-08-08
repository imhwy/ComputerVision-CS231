# import libraries
import cv2
import numpy as np
from math import cos, sin, pi
import matplotlib.pyplot as plt


# loading images and resize
img = cv2.imread("planet.webp")
img = cv2.resize(img, None, fx=1, fy=1)


# visualization the image to get the suitable radius
implot = plt.imshow(img)
plt.show()


# convert image to to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Blur
blur = cv2.medianBlur(gray, 5)


# Canny to detect edge
edges = cv2.Canny(blur, 60, 70)
cv2.imshow("edges image", edges)
cv2.waitKey(0)


# init
circles = []
height, width = img.shape[:2]
minRa = 40
maxRa = 100
H = np.zeros((height, width, maxRa), dtype=np.int32)


# hough(edges, minRadius, maxRadius)
for i in range(height):
    for j in range(width):
        if edges[i][j] == 255:
            for r in range(minRa, maxRa):
                for theta in range(0, 360, 5):
                    temp_i = int(j - r * cos(theta * pi / 180))
                    temp_j = int(i - r * sin(theta * pi / 180))
                    if (
                        temp_i >= 0
                        and temp_j >= 0
                        and temp_i < height
                        and temp_j < width
                    ):
                        H[temp_i, temp_j, r] += 1
    print(i)


print(H.max())
indices = np.where(H >= 35)
for a, b, R in zip(indices[0], indices[1], indices[2]):
    cv2.circle(img, (a, b), R, (0, 255, 0), 1)


# show the image
cv2.imshow("circle detected image", img)
cv2.waitKey(0)


# save the image
cv2.imwrite("result.jpg", img)
