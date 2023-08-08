import cv2

# Load ảnh
img = cv2.imread("a.png")

# Chuyển đổi ảnh sang độ xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng bộ lọc Gaussian để giảm nhiễu
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Phát hiện biên độ với thuật toán Canny
edges = cv2.Canny(gray, 100, 200)i

# Hiển thị ảnh gốc và ảnh phát hiện biên độ
cv2.imshow("Original Image", img)
cv2.imshow("Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
