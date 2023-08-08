# import libraries
import numpy as np
import cv2
from sklearn.linear_model import LogisticRegression


# loading images
scale = 0.25
background_image = cv2.imread("background.png")
background_image = cv2.resize(background_image, None, fx=scale, fy=scale)
objects_image = cv2.imread("object.png")
objects_image = cv2.resize(objects_image, None, fx=scale, fy=scale)
test_image = cv2.imread("test.png")
test_image = cv2.resize(test_image, None, fx=scale, fy=scale)
galaxy_image = cv2.imread("galaxy.jpg")
galaxy_image = cv2.resize(galaxy_image, None, fx=scale, fy=scale)


# Flatten the images into 2D arrays
height, width, channels = background_image.shape
background_flattened = background_image.reshape((height * width, channels))
objects_flattened = objects_image.reshape((height * width, channels))
test_flattened = test_image.reshape((height * width, channels))
galaxy_image = galaxy_image[300 : 300 + height, 60 : 60 + width]


# Create labels for the training data
background_labels = np.zeros(height * width, dtype=np.uint8)
objects_labels = np.ones(height * width, dtype=np.uint8)


# Concatenate the data and labels for training
x_train = np.concatenate((background_flattened, objects_flattened))
y_train = np.concatenate((background_labels, objects_labels))


# Logistic Regression training
LR = LogisticRegression().fit(x_train, y_train)
predict_background = LR.predict_proba(test_flattened)[:, 1]
segmentation_mask = predict_background.reshape((height, width))


# segmentation
# for i in range(0, segmentation_mask.shape[0]):
#     for j in range(0, segmentation_mask.shape[1]):
#         if segmentation_mask[i][j] <= 0.99:
#             test_image[i, j] = galaxy_image[i, j]
# without using loop
alpha = 0.2
test_image[segmentation_mask[:, :] <= 0.99] = (
    alpha * test_image[segmentation_mask[:, :] <= 0.99]
    + (1 - alpha) * galaxy_image[segmentation_mask[:, :] <= 0.99]
)


# show image
cv2.imshow("testing", test_image)
cv2.waitKey(0)
cv2.imwrite("result.png", test_image)
