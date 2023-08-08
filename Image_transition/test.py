import cv2


img = cv2.imread(
    "C:\\UIT\\HK4-II\\Nhap_mon_thi_giac_may_tinh_CS231.N21\\HieuUngHinhAnh\\sourceImages\\pikachu1.jpeg"
)
img2 = cv2.imread(
    "C:\\UIT\\HK4-II\\Nhap_mon_thi_giac_may_tinh_CS231.N21\\HieuUngHinhAnh\\sourceImages\\pikachu2.jpg"
)
h = img.shape[0]
w = img.shape[1]
img2 = cv2.resize(img2, (w, h))
view = img.copy()

# push left
for x in range(img.shape[1]):
    view[:, x:] = img2[:, 0 : img2.shape[1] - x]
    view[:, 0:x] = img2[:, img2.shape[1] - x :]

    cv2.imshow("Wideleft", view)
    cv2.waitKey(1)
