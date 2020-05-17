import cv2
import numpy as np
from sklearn.preprocessing import OneHotEncoder

from traffic_light_classifier.helpers import load_dataset

image_dir = './traffic_light_images/training'
load = load_dataset(image_dir)
image_dir = './traffic_light_images/test'
load.extend(load_dataset(image_dir))

X = np.array([i[0] for i in load])
Y = np.array([i[1] for i in load])


def find_average_width_height(images):
    width = np.average([i.shape[1] for i in images])
    height = np.average([i.shape[0] for i in images])

    return width, height


width, height = find_average_width_height(X)

image_width = int(round(width, 0))
image_height = int(round(height, 0))


def resize_images(images, width=34, height=64):
    return [cv2.resize(image, (width, height)) for image in images]


X = resize_images(X, image_width, image_height)
import matplotlib.pyplot as plt

plt.imshow(X[0])

label_encoder = OneHotEncoder(sparse=False)

print(Y)
Y = label_encoder.fit_transform(Y.reshape((-1, 1)))
print(Y)

categories = {
    label_encoder.categories_[0][0]: [1, 0, 0],
    label_encoder.categories_[0][1]: [0, 1, 0],
    label_encoder.categories_[0][2]: [0, 0, 1]
}
print(categories)


def get_histogram_distribution(images):
    transformed_images = cv2.cvtColor(images, cv2.COLOR_RGB2HSV)

    h = cv2.calcHist(transformed_images, [0], None, [256], [0, 256])
    s = cv2.calcHist(transformed_images, [0], None, [256], [0, 256])
    v = cv2.calcHist(transformed_images, [0], None, [256], [0, 256])

    plt.plot(h, color='r')
    plt.plot(s, color='g')
    plt.plot(v, color='b')

    plt.show()


get_histogram_distribution(X)
