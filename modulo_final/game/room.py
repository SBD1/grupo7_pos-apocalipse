import npc
import inimigo
import weapon
import globals

import pyxel

class Room:
    def __init__(self) -> None:
        self.id = 1
        self.room_tm = []
        self.room_col = []
        self.npcs = []
        self.weapons = []
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

        for weapon in self.weapons:
            weapon.draw()

    def change_room(self, room_id):
        # acessar a sala em questão no banco e a partir dela instanciar tudo o que for necessário (itens, inimigos, npcs...)
        print("trocando sala...")
        self.npcs.clear()
        self.weapons.clear()

        rooms = {
            1: {
                'tm': globals.room1_tm,
                'col': globals.room1_col,
                'npcs': [[5, 2]],
                'inimigos': [[8, 9]],
                'weapons': [[7, 1]],
                'directions': {"up": 0, "down": 2, "left": 0,  "right": 0}
            },
            2: {
                'tm': globals.room2_tm,
                'col': globals.room2_col,
                'npcs': [[2, 9]],
                'inimigos': [[9, 2]],
                'weapons': [[8, 1]],
                'directions': {"up": 1, "down": 0, "left": 0,  "right": 0}
            }
        }

        self.id = room_id
        self.room_tm = rooms[room_id]['tm']
        self.room_col = rooms[room_id]['col']
        self.directions = rooms[room_id]['directions']

        for npc_coords in rooms[room_id]['npcs']:
            self.npcs.append(npc.Npc(*npc_coords)) 

        for inimigo_coords in rooms[room_id]['inimigos']:
            self.npcs.append(inimigo.Inimigo(*inimigo_coords)) 

        for weapon_coords in rooms[room_id]['weapons']:
            self.weapons.append(weapon.Axe(*weapon_coords))
        
        
