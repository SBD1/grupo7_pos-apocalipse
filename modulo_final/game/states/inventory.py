import pyxel

#Local Imports
import utils
import globals
import buttons
from states.gamestate import GameState

# Estado do inventário
class InventoryState(GameState):
    def __init__(self) -> None:
        super().__init__()
        # self.btStart = buttons.PushButton(globals.WIDTH/2, globals.HEIGHT/2, "INICIAR", 15, textCenter=True)

    def update(self):
        super().update()

    def draw(self):
        super().draw()

        pyxel.bltm(0, 0, *[1, 0, 0], globals.WIDTH, globals.HEIGHT)