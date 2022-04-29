import pyxel

#Local Imports
import npc
import weapon
import globals
import queries

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
        if(globals.next_room != None):
            self.change_room(globals.next_room)
            globals.next_room = None
        
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

        change_room = queries.change_room(room_id)
        
        rooms = {
            1: {
                'weapons': [[6, 9]]
            },
            2: {
                'weapons': [[8, 5]]
            }
        }
        self.id = room_id
        self.room_tm = globals.room1_tm if change_room.dados_sala.id == 1 else globals.room2_tm
        self.directions = {"up": change_room.dados_sala.id_norte, "down": change_room.dados_sala.id_sul, "left": change_room.dados_sala.id_oeste, "right": change_room.dados_sala.id_leste}

        for npc_values in change_room.dados_npcs_sala:
            self.npcs.append(npc.Npc(npc_values.id_npc, npc_values.nome, 8, 8, npc_values.vida, npc_values.nivel, npc_values.caracteristica, npc_values.capacidade_carregamento, npc_values.defesa, npc_values.ataque, npc_values.e_hostil, npc_values.id_local, npc_values.id_dialogo, npc_values.id_personagem)) 

        for weapon_values in rooms[room_id]['weapons']:
            self.weapons.append(weapon.Axe(*weapon_values))
        
        
