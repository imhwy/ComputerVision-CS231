# import libraries
import cv2

# loading images
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

# the mid point
mid = int(img1.shape[1] / 2)
a = mid - 1

# width of img1
W = img1.shape[1]

# split img1 to img2 animation
for D in range(mid):
    view = img2.copy()
    view[:, : mid - D] = img1[:, : mid - D]
    view[:, mid + D :] = img1[:, mid + D :]
    cv2.imshow("split animation", view)
    cv2.waitKey(10)

# destroy all window
cv2.destroyAllWindows()
