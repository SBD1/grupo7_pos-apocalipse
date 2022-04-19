import utils
from entity import Entity
import pyxel


class Player(Entity):
    # def __init__(self, x, y):
    #     super().__init__(x, y)

    #     self.x = 128
    #     self.y = 98

    def update(self):
        super().update()

        if pyxel.btn(pyxel.KEY_UP):
            self.dir = "up"
        if pyxel.btn(pyxel.KEY_DOWN):
            self.dir = "down"
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dir = "left"
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dir = "right"

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 40, 0, 8, 8, pyxel.COLOR_BLACK)
