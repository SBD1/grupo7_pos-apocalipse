import pyxel
import math

class Bullet:

    def __init__(self, origin_x, origin_y, target_x, target_y, speed) -> None:
        self.pos_x = origin_x
        self.pos_y = origin_y
        self.vec_x = origin_x - target_x
        self.vec_y = origin_y - target_y
        self.speed = speed
        self.time = 30

        m = math.sqrt(self.vec_x**2 + self.vec_y**2)
        self.vec_x /= m
        self.vec_y /= m

        self.vec_x *= -1
        self.vec_y *= -1

    def update(self):
        self.time -= 1

        self.pos_x+= self.vec_x*self.speed
        self.pos_y+= self.vec_y*self.speed

    def draw(self):
        pyxel.circ(self.pos_x, self.pos_y, 2, pyxel.COLOR_RED)
