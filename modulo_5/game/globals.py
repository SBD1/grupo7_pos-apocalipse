import player
import npc
import inimigo
from states.gamestate import GameState

WIDTH = 128
HEIGHT = 128

next_state = "menu"
current_state = GameState()

player1 = player.Player(32, 32)
npc1 = npc.Npc(40, 16)
inimigo1 = inimigo.Inimigo(64, 72)
