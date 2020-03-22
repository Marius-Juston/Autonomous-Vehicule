from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


class KalmanFilter(ABC):
    @abstractmethod
    def predict(self, motion, motion_uncertainty):
        pass

    @abstractmethod
    def update(self, measurement, measurement_uncertainty):
        pass


class KalmanFilter1D(KalmanFilter):

    def __init__(self, initial_position: float = 0, initial_uncertainty: float = 1e-13) -> None:
        super().__init__()
        self.uncertainty = initial_uncertainty
        self.position = initial_position

        self.states = [[self.position, self.uncertainty]]

    def update(self, measurement, measurement_uncertainty):
        self.position = (measurement * self.uncertainty + self.position * measurement_uncertainty) / \
                        (self.uncertainty + measurement_uncertainty)
        self.uncertainty = 1 / (1 / measurement_uncertainty + 1 / self.uncertainty)

        # self.add_state()

    def predict(self, motion, motion_uncertainty):
        self.uncertainty += motion_uncertainty
        self.position += motion

        self.add_state()

    def add_state(self):
        self.states.append([self.position, self.uncertainty])

    def draw(self):
        blues = plt.get_cmap('Blues')  # this returns a colormap
        # reds = plt.get_cmap('Reds')  # this returns a colormap

        states = self.states[1:]

        for i, (mu, var) in enumerate(states):
            std = np.sqrt(var)
            min_x = mu - 3 * std
            max_x = mu + 3 * std

            x = np.arange(min_x, max_x, 0.01)
            y = norm.pdf(x, mu, std)

            p = float(i) / (len(states) - 1)

            # if i % 2 == 0:
            color = blues(p)  # blues(x) returns a color for each x between 0.0 and 1.0
            # else:
            # color = reds(p)

            plt.plot(x, y, color=color)
            plt.plot([mu, mu], [0, norm.pdf(mu, mu, std)], c=color, linestyle='dashed')


def test_1d():
    measurements = [5., 6., 7., 9., 10.]
    motion = [1., 1., 2., 1., 1.]
    measurement_sig = 4
    motion_sig = 2.
    mu = 0.
    sig = 10.

    kalman_filter = KalmanFilter1D(mu, sig)

    for me, mo in zip(measurements, motion):
        kalman_filter.update(me, measurement_sig)
        kalman_filter.predict(mo, motion_sig)

    print(kalman_filter.position, kalman_filter.uncertainty)
    kalman_filter.draw()
    plt.show()


if __name__ == '__main__':
    test_1d()
