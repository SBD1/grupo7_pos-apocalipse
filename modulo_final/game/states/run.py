import pyxel
import room
import utils
from globals import player1

import globals
from states.gamestate import GameState

# Estado principal onde o jogo em si roda
class RunState(GameState):
    def __init__(self) -> None:
        super().__init__()

        self.room = room.Room()

    def update(self):
        super().update()

        self.room.update()
        
        # player movement
        old_pos = [player1.x, player1.y]
        player1.update()

        if utils.col_player_map(player1.x, player1.y, self.room.room_col):
            player1.x = old_pos[0]
            player1.y = old_pos[1]

        if utils.col_player_map_door(player1.x, player1.y, self.room.room_col):
            player1.x = 7*8+4
            player1.y = 1*8+4
            self.room.change_room(2)

        if pyxel.btnp(pyxel.KEY_B):
            globals.next_state = "menu"

    def draw(self):
        super().draw()

        self.room.draw()
        player1.draw()
