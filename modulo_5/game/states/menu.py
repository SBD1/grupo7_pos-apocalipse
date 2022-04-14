import utils
import globals
import buttons
from states.gamestate import GameState

import pyxel

# Estado Inicial, Menu principal
class MenuState(GameState):
    def __init__(self) -> None:
        super().__init__()
        self.btStart = buttons.PushButton(128, 98, "INICIAR", 25, textCenter=True)

    def update(self):
        super().update()

        if self.btStart.update():
            globals.next_state = "run"

    def draw(self):
        super().draw()

        self.btStart.draw()

        title = 'PROJETO NUCLEAR'
        pyxel.text(utils.align_text(globals.WIDTH/2, title),40, title, 7)