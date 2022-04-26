import pyxel
import globals

def draw_ui():
    ...

def align_text(x, str):
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def get_player_tile(pos_x, pos_y):
    return [int(pos_x/8), int(pos_y/8)]

def get_player_pos(tile_x, tile_y):
    return [int(tile_x*8), int(tile_y*8)]

def get_pos_after_room_change():
   return 1*8+4, 1*8+4

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

def room_change_player_pos(dir):
    return direction_to_position(inv_dir(dir))

def direction_to_position(dir):
    pos = []
    if dir == "right":  pos = get_player_pos(14, 7)
    elif dir == "left": pos = get_player_pos(1, 7)
    elif dir == "up":   pos = get_player_pos(8, 1)
    elif dir == "down": pos = get_player_pos(8, 12)
    return pos

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
