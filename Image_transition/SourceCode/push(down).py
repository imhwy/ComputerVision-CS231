# import libraries
import cv2

# loading the images
img1 = cv2.imread(
    "C:\\UIT\\HK4-II\\Nhap_mon_thi_giac_may_tinh_CS231.N21\\HieuUngHinhAnh\\SourceImages\\pikachu1.jpeg",
    cv2.IMREAD_COLOR,
)
img2 = cv2.imread(
    "C:\\UIT\\HK4-II\\Nhap_mon_thi_giac_may_tinh_CS231.N21\\HieuUngHinhAnh\\SourceImages\\pikachu2.jpg",
    cv2.IMREAD_COLOR,
)

# resize img1 equal to img2
img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# copy of img1
view = img1.copy()

# get the height of img1
H = img1.shape[0]

# push down img1 to img2 animation
for D in range(H):
    view[0:D] = img2[H - D :]
    view[D:] = img1[0 : H - D]
    cv2.imshow("push(down) animation", view)
    cv2.waitKey(10)

# destroy window
cv2.destroyAllWindows()
