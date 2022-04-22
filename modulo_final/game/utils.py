import pyxel

def draw_ui():
    ...

def align_text(x, str):
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def get_player_tile(x, y):
    return [int(x/8), int(y/8)]

def col_player_map(px, py, room_col):
    # print("x = " + str(x))
    # print("y = " + str(y))
    # print("\npx = " + str(px))
    # print("py = " + str(py))
    
    x, y = get_player_tile(px-1, py-1)
    if(room_col[y][x] == 1):
        return True

    x, y = get_player_tile(px+1, py+1)
    if(room_col[y][x] == 1):
        return True

    return False

def col_player_map_door(px, py, room_col):
    x, y = get_player_tile(px-1, py-1)
    if(room_col[y][x] == 2):
        return True

    x, y = get_player_tile(px+1, py+1)
    if(room_col[y][x] == 2):
        return True

    return False

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
