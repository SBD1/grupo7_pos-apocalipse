import pyxel

#Local Imports
from entity import Entity
import utils

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

    def update(self):
        super().update()

    def draw(self):
        npc_draw_args = [self.x-4, self.y-4, 0, 0, 0, 8, 8, pyxel.COLOR_BLACK]
        if self.is_hostile: npc_draw_args[3] = 48
        else: npc_draw_args[3] = 32

        pyxel.blt(*npc_draw_args)
