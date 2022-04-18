import player
import npc
import inimigo
from states.gamestate import GameState

WIDTH = 256
HEIGHT = 196

next_state = "menu"
current_state = GameState()

player1 = player.Player()
npc1 = npc.Npc();
inimigo1 = inimigo.Inimigo();
