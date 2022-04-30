import pyxel
import math

class Bullet:

    def __init__(self, origin_x, origin_y, target_x, target_y, speed, damage = 20, range = 20) -> None:
        self.x = origin_x
        self.y = origin_y
        self.vec_x = origin_x - target_x
        self.vec_y = origin_y - target_y
        self.speed = speed
        self.damage = damage
        self.range = range

        m = math.sqrt(self.vec_x**2 + self.vec_y**2)
        if m != 0: self.vec_x /= m
        if m != 0: self.vec_y /= m

        self.vec_x *= -1
        self.vec_y *= -1

    def update(self):
        self.range -= 1

        self.x+= self.vec_x*self.speed
        self.y+= self.vec_y*self.speed

    def draw(self):
        pyxel.circ(self.x, self.y, 1, pyxel.COLOR_RED)
