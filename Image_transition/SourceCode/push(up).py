# import libraries
import cv2

# loading images
img1 = cv2.imread(
    "C:\\UIT\\HK4-II\\Nhap_mon_thi_giac_may_tinh_CS231.N21\\HieuUngHinhAnh\\SourceImages\\pikachu1.jpeg",
    cv2.IMREAD_COLOR,
)
img2 = cv2.imread(
    "C:\\UIT\\HK4-II\\Nhap_mon_thi_giac_may_tinh_CS231.N21\\HieuUngHinhAnh\SourceImages\\pikachu2.jpg",
    cv2.IMREAD_COLOR,
)

# resize img1 equal to img2
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# copy img1
view = img1.copy()

# get the height of img1
H = img1.shape[0]

# push (down) animation
for D in range(H):
    view[0 : H - D] = img1[D:H]
    view[H - D :] = img2[0:D]
    cv2.imshow("View", view)
    cv2.waitKey(10)

cv2.destroyAllWindows()
