import utils

import pyxel

# Classe abstrata, pai para todos os estados do jogo
class GameState:

    def __init__(self):
        self.timer = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()           

    def draw(self, draw_ui = False):
        pyxel.cls(0)

        if draw_ui :
            utils.draw_ui()