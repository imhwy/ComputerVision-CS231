# import libraries
import cv2

# loading the images
img1 = cv2.imread(
    "C:\\UIT\\HK4-II\\Nhap_mon_thi_giac_may_tinh_CS231.N21\\HieuUngHinhAnh\\source\\pikachu1.jpeg",
    cv2.IMREAD_COLOR,
)
img2 = cv2.imread(
    "C:\\UIT\\HK4-II\\Nhap_mon_thi_giac_may_tinh_CS231.N21\\HieuUngHinhAnh\source\\pikachu2.jpg",
    cv2.IMREAD_COLOR,
)

# resize img1 equal to img2
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))


# get width of img1
W = img1.shape[1]

# wippe img1 to img2 by right to left animation
for D in range(W):
    view = img2.copy()
    view[:, : W - D] = img1[:, : W - D]
    cv2.imshow("wipe (left to right) animation", view)
    cv2.waitKey(10)

# destroy window
cv2.destroyAllWindows()
