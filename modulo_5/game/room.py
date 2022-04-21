import npc
import inimigo
import globals

import pyxel

class Room:
    def __init__(self) -> None:
        self.room_tm = []
        self.room_col = []
        self.npcs = []
        self.items = []
        self.change_room()

    def update(self):
        for npc in self.npcs:
            npc.update()

    def draw(self):
        pyxel.bltm(0, 0, *self.room_tm, globals.WIDTH, globals.HEIGHT)

        for npc in self.npcs:
            npc.draw()

    def change_room(self):
        # acessar a sala em questão no banco e a partir dela instanciar tudo o que for necessário (itens, inimigos, npcs...)
        self.npcs.clear()
        self.items.clear()

        self.room_tm = globals.room1_tm
        self.room_col = globals.room1_col
        self.npcs.append(npc.Npc(5, 2)) 
        self.npcs.append(inimigo.Inimigo(8, 9)) 
