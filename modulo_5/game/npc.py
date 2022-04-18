import utils
from entity import Entity
import pyxel


class Npc(Entity):
    def __init__(self):
        super().__init__()

        self.x = 20
        self.y = 50

    def update(self):
        self.move()

    def draw(self):
        pyxel.circ(self.x, self.y, 10, pyxel.COLOR_YELLOW)
