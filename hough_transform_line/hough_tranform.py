import cv2
import numpy as np
import math


img = cv2.imread("pic.webp")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray, 250, 300, None, 3)


h, w = edges.shape

max_rho = int(math.hypot(h, w))
threshold = 130
max_theta = 360

H = np.zeros((max_theta, max_rho), dtype=np.uint8)

for y in range(h):
    for x in range(w):
        if edges[y, x] > 0:
            for theta in range(max_theta):
                p = int(
                    x * math.cos(math.radians(theta))
                    + y * math.sin(math.radians(theta))
                )
                H[theta, p] += 1

lines = []
for theta in range(max_theta):
    for rho in range(max_rho):
        if H[theta, rho] > threshold:
            # Tính toán tọa độ hai điểm trên đường thẳng
            a = math.cos(math.radians(theta))
            b = math.sin(math.radians(theta))
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            lines.append(((x1, y1), (x2, y2)))

for line in lines:
    cv2.line(img, line[0], line[1], (0, 255, 0), 1)

cv2.imshow("image", img)
cv2.waitKey(0)
