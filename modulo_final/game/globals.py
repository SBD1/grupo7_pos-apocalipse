#Local Imports
import player
import player_weapon
import player_armor
import armor
import queries
from states.gamestate import GameState

WIDTH = 128
HEIGHT = 128

next_state = "menu"
current_state = GameState()

player1 = queries.get_player().toPlayer()

sprites = [
    [32, 56], # 0 hand
    [ 0, 64], # 1 gun
    [72, 72], # 2 shirt
    [72, 56], # 3 armor
    [32, 88], # 4 band-aid
    [56, 64], # 5 potion
]

player_weapon = player_weapon.PlayerWeapon(32, 56, 20, 4)
player_armor  = player_armor.PlayerArmor(72, 72, 5)

# print(player1.x, player1.y)
room_list= []

next_room = None

collision_points = [
[ 1,  3],
[-2,  3],
[ 1, -2],
[-2, -2],
]

# TODO: Acessar o local no banco...
# player1 = player.Player("Sobrevivente", 2, 2)

# TODO: Acessar o terreno no banco para definir o tilemap

room_tms = [
    [0, 0, 0],
    [0, 16*8, 16*8], # 1
    [0, 16*8,    0], # 2
    [0, 16*8, 32*8], # 3
    [0, 0,    32*8], # 4
    [0, 32*8, 32*8], # 5
    [0, 32*8, 16*8], # 6
    [0, 32*8, 48*8], # 7
]
room1_tm = [0, 0, 0]
room2_tm = [0, 16*8, 0]

room_col = [
#                             |   |
#00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15
 [1,  1,  1,  1,  1,  1,  1,  2,  2,  1,  1,  1,  1,  1,  1,  1], #0 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #1 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #2 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #3 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #4 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #5 
 [4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5], #6 ---
 [4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5], #7 ---
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #8 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #9 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #10 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #11 
 [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1], #12 
 [1,  1,  1,  1,  1,  1,  1,  3,  3,  1,  1,  1,  1,  1,  1,  1], #13 
#00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15
#                             |   |
]
