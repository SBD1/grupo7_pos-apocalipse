import pyxel

class PlayerWeapon:
    def __init__(self, img_x, img_y, damage, range):
        self.img_x = img_x
        self.img_y = img_y
        self.damage = damage
        self.range = range

    def draw(self):
        item_draw_args = [50, 119, 0, self.img_x, self.img_y, 8, 8, pyxel.COLOR_BLACK]
        pyxel.blt(*item_draw_args)