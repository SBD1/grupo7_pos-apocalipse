import pyxel

import utils

class Item:
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
        is_equipped):
        self.id = id
        self.peso = peso
        self.nivel = nivel
        self.id_mochila = id_mochila
        self.x = x
        self.y = y
        self.id_local = id_local
        self.id_tipo_item = id_tipo_item
        self.name = name
        self.img_x = img_x
        self.img_y = img_y
        self.type = -1

        self.is_equipped = is_equipped
        
    def update(self):
        ...

    def draw(self):    

        item_draw_args = [self.x-4, self.y-4, 0, self.img_x, self.img_y, 8, 8, pyxel.COLOR_BLACK]
        # print(self.x, self.y)
        pyxel.blt(*item_draw_args)
