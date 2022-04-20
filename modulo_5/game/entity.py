import utils
import pyxel
import globals

# Classe Entidade abstrata, pai para o player, para os npcs e inimigos
class Entity:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.dir = ""

    def update(self):
        self.move()
        self.dir = ""

    def move(self):

        if self.dir == "up":
            if self.y >= 8:
                self.y -= 2

        if self.dir == "down":
            if self.y <= globals.HEIGHT-24:
                self.y += 2

        if self.dir == "left":
            if self.x >= 8:
                self.x -= 2

        if self.dir == "right":
            if self.x <= globals.WIDTH-24:
                self.x += 2
