import utils
import pyxel
import globals

# Classe Entidade abstrata, pai para o player, para os npcs e inimigos
class Entity:
    def __init__(self, x, y) -> None:
        self.x = x*8+4
        self.y = y*8+4
        self.dir = ""
        self.speed = 2

    def update(self):
        self.dir = ""

    def move(self):

        if self.dir == "up":
            self.y -= self.speed

        if self.dir == "down":
            self.y += self.speed

        if self.dir == "left":
            self.x -= self.speed

        if self.dir == "right":
            self.x += self.speed
