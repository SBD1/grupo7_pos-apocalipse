import pyxel

#Local Imports
import globals

def inv_dir(dir):
    new_dir = ""
    if dir == "right": new_dir = "left"
    elif dir == "left": new_dir = "right"
    elif dir == "up": new_dir = "down"
    elif dir == "down": new_dir = "up"

    return new_dir

#################### ACCESSOR UTILS ####################

def get_tile(pos_x, pos_y):
    return [int(pos_x/8), int(pos_y/8)]

def get_screen_pos(tile_x, tile_y):
    return [int(tile_x*8)+4, int(tile_y*8)+4]

#################### COLLISION UTILS ####################

def col_map(px, py):
    x, y = get_tile(px-1, py-1)
    if(globals.room_col[y][x] != 0):
        return globals.room_col[y][x]
    
    x, y = get_tile(px+1, py-1)
    if(globals.room_col[y][x] != 0):
        return globals.room_col[y][x]

    x, y = get_tile(px-1, py+1)
    if(globals.room_col[y][x] != 0):
        return globals.room_col[y][x]

    x, y = get_tile(px+1, py+1)
    if(globals.room_col[y][x] != 0):
        return globals.room_col[y][x]

    # print("nao houve colisao")
    return 0

def col_mouse_bt(mx, my, btx, bty, btw, bth):
    """
        Verifica o clique no botão
    """
    if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
        return True
    else:
        return False

#################### DRAW UTILS ####################

def rect_custom(x1, y1, x2, y2, color):

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    pyxel.rect(x1, y1, x2-x1, y2-y1, color)

def draw_ui():
    ...

def align_text(x, str):
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)