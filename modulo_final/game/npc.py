import pyxel
import random

#Local Imports
from entity import Entity
import utils
import bullet

class Npc(Entity):
    def __init__(self, name, x, y, aggro = False):
        super().__init__(name, x, y)
        self.is_hostile = aggro
        self.going_to1 = ""
        self.going_to2 = ""

    def update(self, player_x = 0, player_y = 0):
        super().update()

        if self.is_hostile:

            if(pyxel.frame_count%30 == 0):
                self.bullets.append(bullet.Bullet(self.x, self.y, player_x, player_y, 2))

            if(pyxel.frame_count%30 == 0):
                self.going_to1 = self.get_direction(random.randint(0, 3))

            self.dir = self.going_to1
            self.move()

            if((pyxel.frame_count+15)%30 == 0):
                self.going_to2 = self.get_direction(random.randint(0, 3))

            if(self.going_to2 != self.going_to1): self.dir = self.going_to2
            self.move()

    def draw(self):
        npc_draw_args = [self.x-4, self.y-4, 0, 0, 0, 8, 8, pyxel.COLOR_BLACK]
        if self.is_hostile: npc_draw_args[3] = 48
        else: npc_draw_args[3] = 32

        pyxel.blt(*npc_draw_args)

        if(self.health < self.total_health):
            utils.draw_health_bar(self.x, self.y, self.total_health, self.health)

        super().draw()
