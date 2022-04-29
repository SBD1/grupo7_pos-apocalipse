import pyxel
import math 

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
        
        player1.update(self.room.directions)

        bullet_to_delete = -1
        npc_to_delete = -1

        for b in player1.bullets:
            for npc in self.room.npcs:

                dist = math.hypot(abs(b.x - npc.x), abs(b.y - npc.y))
                if dist < 5:
                    bullet_to_delete = player1.bullets.index(b)
                    npc.health -= b.damage
                    if(npc.health <= 0):
                        npc_to_delete = self.room.npcs.index(npc)

        if bullet_to_delete != -1:
            del player1.bullets[bullet_to_delete]
        if npc_to_delete != -1:
            del self.room.npcs[npc_to_delete]

        if pyxel.btnp(pyxel.KEY_B):
            globals.next_state = "menu"

        if pyxel.btnp(pyxel.KEY_I):
            globals.next_state = "inventory"

    def draw(self):
        super().draw()

        self.room.draw()
        player1.draw()

        utils.draw_ui()
