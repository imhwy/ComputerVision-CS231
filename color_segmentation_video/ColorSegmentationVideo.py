# import libraries
import numpy as np
import cv2
from sklearn.linear_model import LogisticRegression
import imageio


# resize the material image function
def resize_material(background_image, object1_image, object2_image):
    scale = 0.25
    background_image = cv2.resize(background_image, None, fx=scale, fy=scale)
    object1_image = cv2.resize(object1_image, None, fx=scale, fy=scale)
    object2_image = cv2.resize(object2_image, None, fx=scale, fy=scale)
    return background_image, object1_image, object2_image


# flatten the material image function
def flatten_material(background_image, object1_image, object2_image):
    height, width, channels = background_image.shape
    background_flattened = background_image.reshape((height * width, channels))
    object1_flattened = object1_image.reshape((height * width, channels))
    object2_flattened = object2_image.reshape((height * width, channels))
    return background_flattened, object1_flattened, object2_flattened


# creating the label for material function
def prepare_training_material(
    background_image, background_flattened, object1_flattened, object2_flattened
):
    height, width, chanels = background_image.shape
    background_labels = np.zeros(height * width, dtype=np.uint8)
    object1_labels = np.ones(height * width, dtype=np.uint8)
    object2_labels = np.ones(height * width, dtype=np.uint8)
    x_train = np.concatenate((background_flattened, object1_flattened))
    x_train = np.concatenate((x_train, object2_flattened))
    y_train = np.concatenate((background_labels, object1_labels))
    y_train = np.concatenate((y_train, object2_labels))
    return x_train, y_train


# logistic regression
def logistic_regression(x_train, y_train):
    LR = LogisticRegression().fit(x_train, y_train)
    return LR


# loading video for testing
def main():
    background_image = cv2.imread('background4.png')
    object1_image = cv2.imread('object1.png')
    object2_image = cv2.imread('object2.png')
    background_image, object1_image, object2_image = resize_material(
        background_image, object1_image, object2_image)
    background_flattened, object1_flattened, object2_flattened = flatten_material(
        background_image, object1_image, object2_image
    )
    x_train, y_train = prepare_training_material(
        background_image, background_flattened, object1_flattened, object2_flattened)
    height, width, channels = background_image.shape
    frames = []
    gif = cv2.VideoCapture('giphy.gif')
    while gif.isOpened():
        ret, frame = gif.read()
        if ret:
            frame = cv2.resize(frame, (width, height))
            frames.append(frame)
        else:
            break
    i = 0
    video = cv2.VideoCapture('test2.mp4')
    frames_output = []
    while video.isOpened():
        ret, frame = video.read()
        if ret:
            frame = cv2.resize(frame, (width, height))
            frame_flattened = frame.reshape((height * width, channels))
            predict_background = logistic_regression(
                x_train, y_train).predict_proba(frame_flattened)[:, 1]
            segmentation_mask = predict_background.reshape((height, width))
            alpha = 0
            frame[segmentation_mask[:, :] <= 0.95] = (
                alpha * frame[segmentation_mask[:, :] <= 0.95]
                + (1 - alpha) * frames[i][segmentation_mask[:, :] <= 0.95]
            )
            i += 1
            if i == 27:
                i = 0
        else:
            break
        frames_output.append(frame)
    for i in frames_output:
        cv2.imshow('Frame', i)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


# run code
if __name__ == "__main__":
    main()
