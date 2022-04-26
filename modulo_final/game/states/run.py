import pyxel

#Local Imports
import globals
from globals import player1
from states.gamestate import GameState
import room
import utils

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
            map_col_type = utils.get_map_col_type()

            if(map_col_type == 1):
                player1.x = old_pos[0]
                player1.y = old_pos[1]

            elif(map_col_type >=2 and map_col_type <= 5):

                new_room_id = self.room.directions[utils.int_to_direction(map_col_type)]

                if new_room_id != 0:
                    new_pos = utils.room_change_player_pos(utils.int_to_direction(map_col_type))
                    player1.x = new_pos[0]
                    player1.y = new_pos[1]
                    self.room.change_room(new_room_id)
                else:
                    player1.x = old_pos[0]
                    player1.y = old_pos[1]

        if pyxel.btnp(pyxel.KEY_B):
            globals.next_state = "menu"

        if pyxel.btnp(pyxel.KEY_I):
            globals.next_state = "inventory"

    def draw(self):
        super().draw()

        self.room.draw()
        player1.draw()
