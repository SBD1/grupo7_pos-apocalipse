import pyxel

#Local Imports
from entity import Entity
import weapon
import armor
import bullet
import globals
import queries

import player_weapon
import player_armor

class Player(Entity):

    def __init__(self,
        id_player,
        vida,
        nivel,
        caracteristica,
        capacidade_carregamento,
        defesa,
        ataque,
        nome,
        x,
        y,
        furtividade,
        id_local,
        id_personagem
    ) -> None:
        super().__init__(id_personagem, vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, nome, x, y)
        self.id_player = id_player
        self.furtividade = furtividade
        self.id_local = id_local


    def update(self, room_directions):
        super().update()

        if pyxel.btnp(pyxel.KEY_H):
            self.vida = 100

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.playm(4, loop=False)
            self.bullets.append(bullet.Bullet(self.x, self.y, pyxel.mouse_x, pyxel.mouse_y, 5, globals.player_weapon.damage, globals.player_weapon.range))
            # print(self.bullets[-1].vec_x)
            # print(self.bullets[-1].vec_y)
            # print("click")

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            self.dir = "up"
            self.move(room_directions)
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            self.dir = "down"
            self.move(room_directions)
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.dir = "left"
            self.move(room_directions)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.dir = "right"
            self.move(room_directions)

    def get_item(self, item):
        if (item.__class__.__name__ == "Weapon"):
            globals.player_weapon = player_weapon.PlayerWeapon(*globals.sprites[1], item.damage, item.ammo )
        elif (item.__class__.__name__ == "Armor"):
            globals.player_armor = player_armor.PlayerArmor(*globals.sprites[3], item.defense)
        elif item.__class__.__name__ == "Consumable":
            self.vida = 100
        # queries.get_item(item.id, self.id)

    def draw(self):
        player_draw_args = [self.x-4, self.y-4, 0, 40, 0, 8, 8, pyxel.COLOR_BLACK]
        pyxel.blt(*player_draw_args)

        super().draw()

    def heal(self, heal_int):
        self.vida += heal_int
        if self.vida > self.total_vida: self.vida = self.total_vida