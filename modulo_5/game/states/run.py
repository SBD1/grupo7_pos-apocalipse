import pyxel
import buttons
from globals import player1, npc1, inimigo1

import globals
from states.gamestate import GameState

# Estado principal onde o jogo em si roda


class RunState(GameState):
    def __init__(self) -> None:
        super().__init__()

        self.btBack = buttons.PushButton(15, 15, "<", 5, textCenter=True)

    def update(self):
        super().update()
        player1.update()
        npc1.update()
        inimigo1.update()


        if self.btBack.update():
            globals.next_state = "menu"

    def draw(self):
        super().draw()

        pyxel.bltm(0, 0, 0, 0, 0, globals.WIDTH, globals.HEIGHT)

        player1.draw()
        npc1.draw()
        inimigo1.draw()

        self.btBack.draw()