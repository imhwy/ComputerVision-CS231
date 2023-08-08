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

# copy img1
view = img1.copy()

# get the width of img1
W = img1.shape[1]

# cover animation (right to left)
for D in range(W):
    view[:, W - D :] = img2[:, :D]
    cv2.imshow("The cover animation (left to right)", view)
    cv2.waitKey(10)

# destroy all window
cv2.destroyAllWindows()
