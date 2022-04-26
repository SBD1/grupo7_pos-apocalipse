import pyxel

#Local Imports
from entity import Entity
import utils

class Npc(Entity):
    def __init__(self, name, x, y, aggro):
        super().__init__(name, x, y)
        self.is_hostile = aggro

    def update(self):
        super().update()

    def draw(self):
        npc_draw_args = [self.x-4, self.y-4, 0, 0, 0, 8, 8, pyxel.COLOR_BLACK]
        if self.is_hostile: npc_draw_args[3] = 48
        else: npc_draw_args[3] = 32

        pyxel.blt(*npc_draw_args)
