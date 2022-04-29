import pyxel

#Local Imports
import utils

import queries
import globals

# Classe abstrata, pai para todos os estados do jogo
class GameState:

    def __init__(self):
        self.timer = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            queries.update_player(globals.player1.id, globals.player1.furtividade, globals.player1.x, globals.player1.y, globals.player1.id_local, globals.player1.vida, globals.player1.nivel, globals.player1.caracteristica, globals.player1.capacidade_carregamento, globals.player1.defesa, globals.player1.ataque)
            pyxel.quit()           

    def draw(self, draw_ui = False):
        pyxel.cls(0)

        if draw_ui :
            utils.draw_ui()