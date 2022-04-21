import utils
from entity import Entity
import pyxel


class Inimigo(Entity):
    # def __init__(self):
    #     super().__init__()

    #     self.x = 200
    #     self.y = 175

    def update(self):
        super().update()

    def draw(self):
        pyxel.blt(self.x-4, self.y-4, 0, 48, 0, 8, 8, pyxel.COLOR_BLACK)

