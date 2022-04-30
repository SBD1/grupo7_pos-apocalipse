import pyxel

class PlayerArmor:
    def __init__(self, img_x, img_y, defense):
        self.img_x = img_x
        self.img_y = img_y
        self.defense = defense

    def draw(self):
        item_draw_args = [72, 119, 0, self.img_x, self.img_y, 8, 8, pyxel.COLOR_BLACK]
        pyxel.blt(*item_draw_args)