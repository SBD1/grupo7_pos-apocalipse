import pyxel

#Local Imports
import globals
from globals import player1
from states.gamestate import GameState
import room

# Estado principal onde o jogo em si roda
class RunState(GameState):
    def __init__(self) -> None:
        super().__init__()

        self.room = room.Room()

    def update(self):
        super().update()

        self.room.update()
        
        player1.update(self.room.directions)

        if pyxel.btnp(pyxel.KEY_B):
            globals.next_state = "menu"

        if pyxel.btnp(pyxel.KEY_I):
            globals.next_state = "inventory"

    def draw(self):
        super().draw()

        self.room.draw()
        player1.draw()
