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
        self.change_room(1)

    def update(self):
        for npc in self.npcs:
            npc.update()

    def draw(self):
        pyxel.bltm(0, 0, *self.room_tm, globals.WIDTH, globals.HEIGHT)

        for npc in self.npcs:
            npc.draw()

    def change_room(self, room_id):
        # acessar a sala em questão no banco e a partir dela instanciar tudo o que for necessário (itens, inimigos, npcs...)
        self.npcs.clear()
        self.items.clear()

        rooms = {
            1: {
                'tm': globals.room1_tm,
                'col': globals.room1_col,
                'npcs': [[5, 2]],
                'inimigos': [[8, 9]]
            },
            2: {
                'tm': globals.room2_tm,
                'col': globals.room2_col,
                'npcs': [[2, 9]],
                'inimigos': [[9, 2]]
            }
        }

        self.room_tm = rooms[room_id]['tm']
        self.room_col = rooms[room_id]['col']

        for npc_coords in rooms[room_id]['npcs']:
            self.npcs.append(npc.Npc(npc_coords[0], npc_coords[1])) 

        for inimigo_coords in rooms[room_id]['inimigos']:
            self.npcs.append(inimigo.Inimigo(inimigo_coords[0], inimigo_coords[1])) 
        
        
