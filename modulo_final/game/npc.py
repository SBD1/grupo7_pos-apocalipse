import pyxel
import random

#Local Imports
from entity import Entity
import utils
import bullet

class Npc(Entity):
    def __init__(self, id_npc, name, x, y, 
        vida,
        nivel,
        caracteristica,
        capacidade_carregamento,
        defesa,
        ataque,
        aggro,
        id_local,
        id_dialogo,
        id_personagem
        ):
        super().__init__(id_personagem, vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, name, x, y)
        self.id_npc = id_npc
        self.is_hostile = aggro
        self.id_local = id_local
        self.id_dialogo = id_dialogo
        self.going_to1 = ""
        self.going_to2 = ""

    def update(self, player_x = 0, player_y = 0):
        super().update()

        if self.is_hostile:

            if(pyxel.frame_count%30 == 0):
                pyxel.playm(4, loop=False)
                self.bullets.append(bullet.Bullet(self.x, self.y, player_x, player_y, 2, self.ataque))

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

        if(self.vida < self.total_vida):
            utils.draw_health_bar(self.x, self.y, self.total_vida, self.vida)

        super().draw()
