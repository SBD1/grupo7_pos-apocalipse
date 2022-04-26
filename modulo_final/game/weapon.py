
from item import Entity
import pyxel


class Weapon(Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)
        
        self.type = self.TYPE_WEAPON
    
    def update(self, map):
        pass

    def draw():
        super().draw()
        
class Club(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Club", 0, 64, 32, tile_x*8, tile_y*8)
    
    def draw(self):
        pyxel.blt(self.tile_x*8, self.tile_y*8, 0, 64, 32, 8, 8, pyxel.COLOR_BLACK)
        
class Sword(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Sword", 0, 48, 32, tile_x*8, tile_y*8)

    def draw(self):
        pyxel.blt(self.tile_x, self.tile_y, 0, 48, 32, 8, 8, pyxel.COLOR_BLACK)
        
class Axe(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Axe", 0, 56, 32, tile_x*8, tile_y*8)

    def draw(self):
        pyxel.blt(self.tile_x-4, self.tile_y-4, 0, 56, 32, 8, 8, pyxel.COLOR_BLACK)
        
