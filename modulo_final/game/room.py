import pyxel

#Local Imports
import npc
import weapon
import globals

class Room:
    def __init__(self) -> None:
        self.id = 1
        self.room_tm = []
        self.npcs = []
        self.weapons = []
        self.items = []
        self.directions = {}
        self.change_room(1)

    def update(self):
        if(globals.next_room != 0):
            self.change_room(globals.next_room)
            globals.next_room = 0
        
        for npc in self.npcs:
            npc.update(globals.player1.x, globals.player1.y)

    def draw(self):
        pyxel.bltm(0, 0, *self.room_tm, globals.WIDTH, globals.HEIGHT)

        for npc in self.npcs:
            npc.draw()

        for weapon in self.weapons:
            weapon.draw()

    def change_room(self, room_id):
        # TODO: Acessar o local no banco e instanciar tudo o que for necessário (itens, inimigos, npcs...)
        # print("trocando sala...")
        self.npcs.clear()
        self.weapons.clear()

        rooms = {
            1: {
                'tm': globals.room1_tm,
                'npcs': [["Viajante", 5, 2, False], ["Bandido", 8, 9, True]],
                'weapons': [[6, 9]],
                'directions': {"up": 0, "down": 2, "left": 1,  "right": 1}
            },
            2: {
                'tm': globals.room2_tm,
                'npcs': [["Andarilho", 2, 9, False], ["Malfeitor", 9, 2, True]],
                'weapons': [[8, 5]],
                'directions': {"up": 1, "down": 0, "left": 0,  "right": 0}
            }
        }

        self.id = room_id
        self.room_tm = rooms[room_id]['tm']
        self.directions = rooms[room_id]['directions']

        for npc_values in rooms[room_id]['npcs']:
            self.npcs.append(npc.Npc(*npc_values)) 

        for weapon_values in rooms[room_id]['weapons']:
            self.weapons.append(weapon.Axe(*weapon_values))
        
        
