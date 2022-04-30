import pyxel

#Local Imports
import utils
import globals
import buttons
from states.gamestate import GameState


# Estado Inicial, Menu principal
class GameOverState(GameState):
    def __init__(self) -> None:
        super().__init__()
        self.btRetry = buttons.PushButton(globals.WIDTH/2, globals.HEIGHT/2, "VOLTAR?", 15, True, 8, 2)
        globals.next_room = 1
        globals.player1.vida = 100

    def update(self):
        super().update()

        if self.btRetry.update():
            globals.next_state = "menu"

    def draw(self):
        super().draw()

        self.btRetry.draw()

        title = 'VOCE MORREU'
        pyxel.text(utils.align_text(globals.WIDTH/2, title), 20, title, 7)