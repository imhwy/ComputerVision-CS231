import numpy as np
import cv2

# Đọc ảnh đầu vào
img = cv2.imread("a.png", cv2.IMREAD_GRAYSCALE)

# Tạo kernel Sobel dọc và ngang
kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Áp dụng kernel Sobel để tính toán đạo hàm theo chiều ngang và dọc
G_x = cv2.filter2D(img, -1, kernel_x)
G_y = cv2.filter2D(img, -1, kernel_y)

# Tính toán độ lớn của gradient và hướng
G = np.sqrt(np.square(G_x) + np.square(G_y))
G = np.uint8(G / np.max(G) * 255)
theta = np.arctan2(G_y, G_x)

# Chuyển đổi hướng từ radian sang độ và đưa về khoảng giá trị 0-180
theta = np.rad2deg(theta)
theta[theta < 0] += 180

# Đặt ngưỡng để phân loại pixel là biên cạnh hoặc không phải biên cạnh
threshold = 100
edge_img = np.zeros_like(G)
edge_img[G > threshold] = 255

# Hiển thị ảnh đầu vào và ảnh biên cạnh
# cv2.imshow('Input Image', img)
cv2.imshow("Edge Image", edge_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
