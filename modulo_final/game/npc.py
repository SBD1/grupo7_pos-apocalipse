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
        npc_draw_args = [self.x-4, self.y-4, 0, 32, 0, 8, 8, pyxel.COLOR_BLACK]
        pyxel.blt(*npc_draw_args)
