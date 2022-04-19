import utils
from entity import Entity
import pyxel


class Npc(Entity):
    # def __init__(self, x, y):
    #     super().__init__()

    #     self.x = 20
    #     self.y = 50

    def update(self):
        super().update()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 0, 8, 8, pyxel.COLOR_BLACK)

