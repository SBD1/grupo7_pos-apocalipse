import utils
from entity import Entity
import pyxel


class Player(Entity):

    def update(self):
        super().update()

        if pyxel.btn(pyxel.KEY_UP):
            self.dir = "up"
            self.move()
        if pyxel.btn(pyxel.KEY_DOWN):
            self.dir = "down"
            self.move()
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dir = "left"
            self.move()
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dir = "right"
            self.move()

    def draw(self):
        player_draw_args = [self.x-4, self.y-4, 0, 40, 0, 8, 8, pyxel.COLOR_BLACK]
        pyxel.blt(*player_draw_args)
