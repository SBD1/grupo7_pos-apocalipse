import pyxel

#Local Imports
from item import Item

class Armor(Item):
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
        id_armadura,
        defense,
        material,
        condition):
        super().__init__(id, peso, nivel, id_mochila, x, y, id_local, id_tipo_item, name, img_x, img_y, is_equipped)
        
        self.id_armadura = id_armadura 
        self.defense = defense
        self.material = material
        self.condition = condition

    def update(self):
        super().update()

    def draw(self):
        # if self.is_equipped:
        #     item_draw_args = [70, 115, 0, self.img_x, self.img_y, 8, 8, pyxel.COLOR_BLACK]
        #     pyxel.blt(*item_draw_args)
        # else:
        super().draw()
        