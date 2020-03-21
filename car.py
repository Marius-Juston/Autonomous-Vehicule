from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


class AbstractCar(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.ax = self.configure_world()

    def configure_world(self):
        ax: Axes = plt.gca()
        ax.grid(True)
        ax.set_facecolor("black")
        ax.set_aspect("equal")
        plt.tight_layout()

        return ax

    @abstractmethod
    def _draw_world(self, *args):
        pass

    @abstractmethod
    def display_world(self):
        pass


class DeterministicCar(AbstractCar):
    @abstractmethod
    def move(self, dt):
        pass

    @abstractmethod
    def turn(self, dtheta):
        pass

    def _draw_world(self, xs, ys, vx, vy):
        self.ax.scatter(xs[:-1],
                        ys[:-1],
                        c=np.linspace(0, 2 * np.pi, xs[:-1].shape[0]),
                        cmap='hsv',
                        s=2 ** 3)
        # self.ax.scatter(self.positions[-1:, 0], self.positions[-1:, 1], c='red', marker='x', s=2 ** 7)
        self.ax.arrow(xs[-1],
                      ys[-1],
                      vx,
                      vy,
                      color='red',
                      width=.25)


class Car(DeterministicCar):
    def __init__(self, position=None, velocity=None, acceleration=None) -> None:
        super().__init__()
        if velocity is None:
            self.velocity = np.zeros(2)
        else:
            self.velocity = np.asarray(velocity)

        if acceleration is None:
            self.acceleration = np.zeros(2)
        else:
            self.acceleration = np.asarray(acceleration)

        if position is None:
            self.position = np.zeros(2)
        else:
            self.position = np.asarray(position)

        self.positions = np.array([self.position])

    def get_state(self):
        return np.array((self.position, self.velocity, self.acceleration))

    state = property(get_state)

    def move(self, dt):
        self.position = self.position + self.velocity * dt + .5 * self.acceleration * dt ** 2
        self.velocity = self.velocity + self.acceleration * dt

        self.positions = np.append(self.positions, [self.position], axis=0)

    def display_world(self):
        self._draw_world(self.positions[:, 0], self.positions[:, 1], *self.velocity)

    def turn(self, dangle):
        dangle = -np.deg2rad(dangle)

        rotation_matrix = np.array([[np.cos(dangle), -np.sin(dangle)], [np.sin(dangle), np.cos(dangle)]])

        self.velocity = np.matmul(rotation_matrix, self.velocity)


class MatrixCar(DeterministicCar):

    def move(self, dt):
        self.state = np.matmul(self.get_transformation_matrix(dt), self.state)

        self.states = np.append(self.states, [self.state], axis=0)

    def turn(self, dtheta):
        self.state = np.matmul(self.get_turn_matrix(dtheta), self.state)

    def __init__(self, state=None) -> None:
        super().__init__()
        if state is None:
            self.state = np.zeros((6, 1))
        else:
            self.state = np.asarray(state)
            self.state = self.state.reshape((6, 1))

        self.states = np.reshape(self.state, (1, *self.state.shape))

    def get_transformation_matrix(self, dt):
        return np.array([
            [1, dt, .5 * dt ** 2, 0, 0, 0],
            [0, 1, dt, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, dt, .5 * dt ** 2],
            [0, 0, 0, 0, 1, dt],
            [0, 0, 0, 0, 0, 1],
        ])

    def get_turn_matrix(self, dangle):
        dangle = -np.deg2rad(dangle)

        c, s = np.cos(dangle), np.sin(dangle)
        return np.array([
            [1, 0, 0, 0, 0, 0],
            [0, c, 0, 0, -s, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, s, 0, 0, c, 0],
            [0, 0, 0, 0, 0, 1]
        ])

    def display_world(self):
        self._draw_world(self.states[:, 0, 0], self.states[:, 3, 0], self.states[-1, 1, 0],
                         self.states[-1, 4, 0])


