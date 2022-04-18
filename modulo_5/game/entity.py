import utils
import pyxel

# Classe Entidade abstrata, pai para o player, para os npcs e inimigos
class Entity:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def move(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 5
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 5
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 5
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 5
