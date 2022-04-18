import utils
from entity import Entity
import pyxel


class Inimigo(Entity):
    def __init__(self):
        super().__init__()

        self.x = 200
        self.y = 175

    def update(self):
        self.move()

    def draw(self):
        pyxel.circ(self.x, self.y, 10, pyxel.COLOR_RED)
