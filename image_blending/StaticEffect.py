# import libraries
import cv2
import math
import numpy as np


# loading 3 images include(foreground, mask and effect images)
fg_img = cv2.imread("foreground.jpg", cv2.IMREAD_COLOR)
mask_img = cv2.imread("mask.png", cv2.IMREAD_UNCHANGED)
eff_img = cv2.imread("effect.jpeg", cv2.IMREAD_COLOR)


# resize the images
fg_img = cv2.resize(fg_img, (600, 600))
mask_img = cv2.resize(mask_img, (600, 600))
eff_img = cv2.resize(eff_img, (fg_img.shape[1], fg_img.shape[0]))


# sigmod function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# static effect with loop
result_1 = fg_img.copy()
alpha_channel = mask_img[:, :, -1]
for index1, row in enumerate(alpha_channel):
    percent = sigmoid(1 - index1 / alpha_channel.shape[0])
    for index2, column in enumerate(row):
        if column != 0:
            result_1[index1, index2] = (
                percent * fg_img[index1, index2]
                + (1 - percent) * eff_img[index1, index2]
            )
        else:
            result_1[index1, index2] = eff_img[index1, index2]


# create a list which pass sigmoid function
matrix = np.linspace(1, 0, 600 * 600).reshape(600, 600)
tensor = np.repeat(matrix[..., np.newaxis], 3, axis=-1)
sigmoid_matrix = sigmoid(tensor)


# static effect with no loop
result_2 = fg_img.copy()
alpha = 0.1
result_2[mask_img[:, :, 3] != 0] = fg_img[mask_img[:, :, 3] != 0] * alpha + eff_img[
    mask_img[:, :, 3] != 0
] * (1 - alpha)

# run code
def main():
    options = int(input("1. static effect with loop\n2. static effect with no loop\n"))
    if options == 1:
        cv2.imshow("static effect with loop", result_1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif options == 2:
        cv2.imshow("static effect with no loop", result_2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("invalid options(out of 1 or 2) please run code again")


if __name__ == "__main__":
    main()
