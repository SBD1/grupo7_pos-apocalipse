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

    # print("\ncollision checking for points:")
    # for point in collision_points:
    #     print([point[0]+px, point[1]+py])

    for point in globals.collision_points:
        x, y = get_tile(point[0]+px, point[1]+py)
        if(globals.room_col[y][x] != 0):
            return globals.room_col[y][x]

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

def draw_health_bar(x, y, total_health, current_health, is_thick = False, size = 10):
    
    length = size
    start = x-5
    height = y+6

    current_length = (length*current_health)/total_health

    l_start = [start,  height]
    l_end1 =   [start+length, height]
    l_end2 =   [start+current_length, height]

    if(is_thick):
        pyxel.line(l_start[0], l_start[1]-1, l_end1[0], l_end1[1]-1, pyxel.COLOR_WHITE)
        pyxel.line(l_start[0], l_start[1],   l_end1[0], l_end1[1],   pyxel.COLOR_WHITE)
        pyxel.line(l_start[0], l_start[1]+1, l_end1[0], l_end1[1]+1, pyxel.COLOR_WHITE)
        
        pyxel.line(l_start[0], l_start[1]-1, l_end2[0], l_end2[1]-1, pyxel.COLOR_RED)
        pyxel.line(l_start[0], l_start[1],   l_end2[0], l_end2[1],   pyxel.COLOR_RED)
        pyxel.line(l_start[0], l_start[1]+1, l_end2[0], l_end2[1]+1, pyxel.COLOR_RED)
    else:
        pyxel.line(*l_start, *l_end1, pyxel.COLOR_WHITE)
        pyxel.line(*l_start, *l_end2, pyxel.COLOR_RED)

def draw_ui():
    draw_health_bar(10, 114, globals.player1.total_health, globals.player1.health, True, 30)
    # globals.player1.x

def align_text(x, str):
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)