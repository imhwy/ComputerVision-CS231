# Import libraries
import numpy as np
import cv2
from scipy.ndimage.filters import convolve
from tqdm import trange
from numba import jit


# Calculate the energy
def energy_image(image):
    dy = np.array(
        [
            [1.0, 2.0, 1.0],
            [0.0, 0.0, 0.0],
            [-1.0, -2.0, -1.0],
        ]
    )
    dx = np.array(
        [
            [1.0, 0.0, -1.0],
            [2.0, 0.0, -2.0],
            [1.0, 0.0, -1.0],
        ]
    )
    dx = np.stack([dx] * 3, axis=2)
    dy = np.stack([dy] * 3, axis=2)
    image = image.astype("float32")
    convolved = np.absolute(convolve(image, dx)) + np.absolute(convolve(image, dy))
    energy = convolved.sum(axis=2)
    return energy


# Find the seam which least energy
@jit
def finding_seam(image):
    h, w, _ = image.shape
    energy = energy_image(image)
    S = energy.copy()
    backward = np.zeros_like(S, dtype=np.int)
    for i in range(1, h):
        for j in range(0, w):
            if j == 0:
                idx = np.argmin(S[i - 1, j : j + 2]) 
                backward[i, j] = idx + j
                min_energy = S[i - 1, idx + j]
            else:
                idx = np.argmin(S[i - 1, j - 1 : j + 2])
                backward[i, j] = idx + j - 1
                min_energy = S[i - 1, idx + j - 1]
            S[i, j] += min_energy
    return S, backward


# Delete the seam from the image
def delete_seam(image):
    h, w, _ = image.shape
    S, backward = finding_seam(image)
    mask = np.ones((h, w), dtype=np.bool)
    j = np.argmin(S[-1])
    for i in reversed(range(h)):
        mask[i, j] = False
        j = backward[i, j]
    mask = np.stack([mask] * 3, axis=2)
    image = image[mask].reshape((h, w - 1, 3))
    return image


# Looping through columns
def croping_image(image, scale_w):
    _, w, _ = image.shape
    newW = int(scale_w * w)
    for i in trange(w - newW):
        image = delete_seam(image)
    return image


# run code
def main():
    image = cv2.imread("test_image.jpg")
    w_input = float(input("input the percentage of width [0-1]: "))
    output_image = croping_image(image, w_input)
    print(image.shape)
    print(output_image.shape)
    cv2.imshow("testing", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
