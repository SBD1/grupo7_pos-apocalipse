import pyxel

#Local Imports
import npc
import weapon
import globals
import queries
import weapon
import armor
import consumable

class Room:
    def __init__(self) -> None:
        self.id = 1
        self.room_tm = []
        self.npcs = []
        # self.weapons = []
        self.items = []
        self.directions = {}
        self.change_room(globals.player1.id_local)

    def update(self):
        if(globals.next_room != None):
            self.change_room(globals.next_room)
            globals.next_room = None
        
        for npc in self.npcs:
            npc.update(globals.player1.x, globals.player1.y)

        for item in self.items:
            item.update()

    def draw(self):
        pyxel.bltm(0, 0, *self.room_tm, globals.WIDTH, globals.HEIGHT)

        for npc in self.npcs:
            npc.draw()

        for item in self.items:
            item.draw()

    def change_room(self, room_id):
        # TODO: Acessar o local no banco e instanciar tudo o que for necessário (itens, inimigos, npcs...)
        print("trocando sala...")
        print(room_id)
        globals.player1.id_local = room_id
        
        self.npcs.clear()
        self.items.clear()

        change_room = queries.change_room(room_id)

        self.id = room_id
        self.room_tm = globals.room_tms[room_id] # if change_room.dados_sala.id == 1 else globals.room2_tm
        self.directions = {"up": change_room.dados_sala.id_norte, "down": change_room.dados_sala.id_sul, "left": change_room.dados_sala.id_oeste, "right": change_room.dados_sala.id_leste}

        for npc_values in change_room.dados_npcs_sala:
            self.npcs.append(npc.Npc(npc_values.id_npc, npc_values.nome, npc_values.x, npc_values.y, npc_values.vida, npc_values.nivel, npc_values.caracteristica, npc_values.capacidade_carregamento, npc_values.defesa, npc_values.ataque, npc_values.e_hostil, npc_values.id_local, npc_values.id_dialogo, npc_values.id_personagem)) 

        # self.items.append(weapon.Weapon(arma.id, arma.peso, arma.nivel, arma.id_mochila, arma.coordenadax, arma.coordenaday, arma.id_local, arma.id_tipo_item, 'arma', *globals.sprites[1], 0, arma.id_arma, arma.dano, arma.descricao, arma.durabilidade, arma.municao))
        for arma in change_room.dados_armas_sala:
            print("arma")
            self.items.append(weapon.Weapon(arma.id, arma.peso, arma.nivel, arma.id_mochila, arma.coordenadax, arma.coordenaday, arma.id_local, arma.id_tipo_item, 'arma', *globals.sprites[1], 0, arma.id_arma, arma.dano, arma.descricao, arma.durabilidade, arma.municao))
                
        for armadura in change_room.dados_armaduras_sala:
            print("armadura")
            self.items.append(armor.Armor(armadura.id, armadura.peso, armadura.nivel, armadura.id_mochila, armadura.coordenadax, armadura.coordenaday, armadura.id_local, armadura.id_tipo_item, 'armadura', *globals.sprites[3], 0, armadura.id_armadura, armadura.defesa, armadura.material, armadura.durabilidade))

        # change_room.dados_itens_sala.
        for consumivel in change_room.dados_consumiveis_sala:
            print("cons")
            self.items.append(consumable.Consumable(consumivel.id, consumivel.peso, consumivel.nivel, consumivel.id_mochila, consumivel.coordenadax, consumivel.coordenaday, consumivel.id_local, consumivel.id_tipo_item, 'consumivel', *globals.sprites[4], 0, consumivel.id_consumivel, consumivel.descricao, consumivel.efeito, consumivel.valor))
        
        
