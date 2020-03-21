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

