import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OneHotEncoder

from traffic_light_classifier.helpers import load_dataset


def find_average_width_height(images):
    width = np.average([i.shape[1] for i in images])
    height = np.average([i.shape[0] for i in images])

    return width, height


def resize_images(images, width=34, height=64):
    return np.stack([cv2.resize(image, (width, height)) for image in images])


def get_histogram_distribution(images, ax=None):
    sum_a = np.zeros((256, 256))
    sum_b = np.zeros((256, 256))
    sum_c = np.zeros((256, 256))

    for image in images:
        transformed_images = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

        # a = cv2.calcHist(transformed_images, [0], None, [256], [0, 256])
        b = cv2.calcHist(transformed_images, [1], None, [256], [0, 256])
        c = cv2.calcHist(transformed_images, [2], None, [256], [0, 256])

        # sum_a += a
        sum_b += b
        sum_c += c

    l = len(images)

    if ax is None:
        plt.plot(sum_a / l, color='r')
        plt.plot(sum_b / l, color='g')
        plt.plot(sum_c / l, color='b')

        plt.show()
    else:
        ax.plot(sum_a / l, color='r')
        ax.plot(sum_b / l, color='g')
        ax.plot(sum_c / l, color='b')


def get_data(data, category, label, categories):
    return data[np.all(label == categories[category], axis=1)]


if __name__ == '__main__':
    image_dir = './traffic_light_images/training'
    load = load_dataset(image_dir)
    image_dir = './traffic_light_images/test'
    load.extend(load_dataset(image_dir))

    X = [i[0] for i in load]
    Y = np.array([i[1] for i in load])

    width, height = find_average_width_height(X)

    image_width = int(round(width, 0))
    image_height = int(round(height, 0))

    X = resize_images(X, image_width, image_height)

    # plt.imshow(X[0])
    # plt.show()

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

    get_histogram_distribution(X[np.all(Y == categories['red'], axis=1)])
