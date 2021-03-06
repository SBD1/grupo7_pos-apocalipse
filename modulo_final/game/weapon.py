import pyxel

#Local Imports
from item import Item

class Weapon(Item):
    def __init__(self,
        id,
        peso,
        nivel,
        id_mochila,
        x,
        y,
        id_local,
        id_tipo_item,
        name,
        img_x,
        img_y,
        is_equipped,
        id_arma,
        damage,
        description,
        condition,
        ammo):
        super().__init__(id, peso, nivel, id_mochila, x, y, id_local, id_tipo_item, name, img_x, img_y, is_equipped)
        
        self.id_arma = id_arma 
        self.damage = damage
        self.description = description
        self.condition = condition
        self.ammo = ammo

    def update(self):
        super().update()

    def draw(self):

        # if self.is_equipped:
        #     item_draw_args = [50, 115, 0, self.img_x, self.img_y, 8, 8, pyxel.COLOR_BLACK]
        #     pyxel.blt(*item_draw_args)
        # else:
        super().draw()
        