from lib2to3.pytree import convert
import pyxel
from sqlalchemy import true
import globals

def draw_ui():
    ...

def align_text(x, str):
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def get_player_tile(x, y):
    return [int(x/8), int(y/8)]

def col_player_map(px, py, room_col):
    x, y = get_player_tile(px-1, py-1)
    if(room_col[y][x] != 0):
        update_map_col_type(room_col[y][x])
        return True
    
    x, y = get_player_tile(px+1, py-1)
    if(room_col[y][x] != 0):
        update_map_col_type(room_col[y][x])
        return True

    x, y = get_player_tile(px-1, py+1)
    if(room_col[y][x] != 0):
        update_map_col_type(room_col[y][x])
        return True

    x, y = get_player_tile(px+1, py+1)
    if(room_col[y][x] != 0):
        update_map_col_type(room_col[y][x])
        return True

    # print("nao houve colisao")
    update_map_col_type(0)
    return False

def update_map_col_type(type):
    globals.current_map_col_type = type

def get_map_col_type():
    return globals.current_map_col_type

def int_to_direction(dir_int):
    if(dir_int == 2): return "up"
    elif(dir_int == 3): return "down"
    elif(dir_int == 4): return "left"
    elif(dir_int == 5): return "right"
    else: return "null"

def col_mouse_bt(mx, my, btx, bty, btw, bth):
    """
        Verifica o clique no botão
    """
    if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
        return True
    else:
        return False

def inv_dir(dir):
    new_dir = ""
    if dir == "right": new_dir = "left"
    elif dir == "left": new_dir = "right"
    elif dir == "up": new_dir = "down"
    elif dir == "down": new_dir = "up"

    return new_dir

def rect_custom(x1, y1, x2, y2, color):

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    pyxel.rect(x1, y1, x2-x1, y2-y1, color)
