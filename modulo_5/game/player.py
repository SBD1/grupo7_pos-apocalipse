import utils
from entity import Entity
import pyxel


class Player(Entity):
    def __init__(self):
        super().__init__()

        self.x = 128
        self.y = 98

    def update(self):
        self.move()

    def draw(self):
        pyxel.circ(self.x, self.y, 10, pyxel.COLOR_WHITE)
