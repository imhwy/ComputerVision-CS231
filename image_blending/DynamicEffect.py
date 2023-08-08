# import libraries
import cv2
import imageio


# loading 3 images include(foreground, mask and effect images)
fg_img = cv2.imread("foreground.jpg", cv2.IMREAD_COLOR)
mask_img = cv2.imread("mask.png", cv2.IMREAD_UNCHANGED)
fg_img = cv2.resize(fg_img, (450, 450))
mask_img = cv2.resize(mask_img, (450, 450))


# gif
url = "https://media2.giphy.com/media/l0HlLP5fowu9vAbUk/giphy.gif?cid=ecf05e47803c3756rfxk5c5sooayr0pbdn6l6v7tv0zhhzy6&rid=giphy.gif&ct=g"
frames = imageio.mimread(imageio.core.urlopen(url).read(), ".gif")


# cutting
fg_h, fg_w, fg_c = fg_img.shape
bg_h, bg_w, bg_c = frames[0].shape
top = int((bg_h - fg_h) / 2)
left = int((bg_w - fg_w) / 2)
bgs = [frame[top : top + fg_h, left : left + fg_w, 0:3] for frame in frames]


# dynamic effects
results = []
alpha = 0.3
for i in range(len(bgs)):
    result = fg_img.copy()
    result[mask_img[:, :, 3] != 0] = alpha * result[mask_img[:, :, 3] != 0]
    bgs[i][mask_img[:, :, 3] == 0] = 0
    bgs[i][mask_img[:, :, 3] != 0] = (1 - alpha) * bgs[i][mask_img[:, :, 3] != 0]
    result = result + bgs[i]
    results.append(result)


# save effect
imageio.mimsave("result.gif", results)
