from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
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


