import pyxel
import buttons

import globals
from states.gamestate import GameState

# Estado principal onde o jogo em si roda
class RunState(GameState):
    def __init__(self) -> None:
        super().__init__()
        self.x = 40
        self.y = 40

        self.btBack = buttons.PushButton(15, 15, "<", 5, textCenter=True)


    def update(self):
        super().update()
        
        if self.btBack.update():
            globals.next_state = "menu"

        if pyxel.btn(pyxel.KEY_UP):
            self.y-=5
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y+=5
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x-=5
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x+=5
            
    def draw(self):
        super().draw()

        self.btBack.draw()

        pyxel.circ(self.x, self.y, 10, pyxel.COLOR_YELLOW)