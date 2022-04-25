import npc
import enemy
import globals

import pyxel

class Room:
    def __init__(self) -> None:
        self.room_tm = []
        self.room_col = []
        self.npcs = []
        self.items = []
        self.directions = {}
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
        print("trocando sala...")
        self.npcs.clear()
        self.items.clear()

        rooms = {
            1: {
                'tm': globals.room1_tm,
                'col': globals.room1_col,
                'npcs': [[5, 2]],
                'inimigos': [[8, 9]],
                'directions': {"up": 0, "down": 2, "left": 0,  "right": 0}
            },
            2: {
                'tm': globals.room2_tm,
                'col': globals.room2_col,
                'npcs': [[2, 9]],
                'inimigos': [[9, 2]],
                'directions': {"up": 1, "down": 0, "left": 0,  "right": 0}
            }
        }

        self.room_tm = rooms[room_id]['tm']
        self.room_col = rooms[room_id]['col']
        self.directions = rooms[room_id]['directions']

        for npc_coords in rooms[room_id]['npcs']:
            self.npcs.append(npc.Npc(npc_coords[0], npc_coords[1])) 

        for inimigo_coords in rooms[room_id]['inimigos']:
            self.npcs.append(enemy.Enemy(inimigo_coords[0], inimigo_coords[1])) 
        
        
