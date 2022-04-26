import utils
from entity import Entity
import pyxel
import bullet


class Player(Entity):

    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.bullets = []

    def update(self):
        super().update()

        for blt in self.bullets:
            blt.update()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.bullets.append(bullet.Bullet(self.x, self.y, pyxel.mouse_x, pyxel.mouse_y, 2))
            print(self.bullets[-1].vec_x)
            print(self.bullets[-1].vec_y)
            print("click")

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            self.dir = "up"
            self.move()
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            self.dir = "down"
            self.move()
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.dir = "left"
            self.move()
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.dir = "right"
            self.move()

    def draw(self):
        player_draw_args = [self.x-4, self.y-4, 0, 40, 0, 8, 8, pyxel.COLOR_BLACK]
        pyxel.blt(*player_draw_args)

        for blt in self.bullets:
            blt.draw()
