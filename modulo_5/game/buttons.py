from math import dist
import pyxel

from utils import align_text, col_mouse_bt
# Evitando import circular:
 
# def align_text(x, str):
#     """
#         Função que alinha o texto dos botões

#         Params: x: int, str: String
#         Return: x: int
#     """
#     n = len(str)
#     return (x - (n * pyxel.FONT_WIDTH) / 2)

# def col_mouse_bt(mx, my, btx, bty, btw, bth):
#     """
#         Verifica o clique no botão
#     """
#     if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
#         return True
#     else:
#         return False

# Fim da seção usada para evitar import circular


# Classe Button abstrata, pai de todos os outros buttons
class Button:

    def __init__(self, x, y, text):
        self.posx = x
        self.posy = y
        self.text = text
        self.offset = 4
        self.is_on = False
        self.color = 0
        self.subcolor = 0
        self.textCenter = False
        self.description = ""

    def update(self):
        """Atualiza o estado do botão"""
        ...

    def draw(self):
        """Desenha o botão na tela"""
        ...
        
class CircleButton(Button):
    def __init__(self, x, y, text, r=15, textCenter=False):
        super().__init__(x, y, text, )
        self.color = 10
        self.subcolor = 9
        self.radius = r
        self.textCenter = textCenter
        
    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        bpos = [self.posx, self.posy]

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 0
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            if self.is_on:
                self.is_on = False
                self.offset = 4
            else:
                self.is_on = True
                self.offset = 2

            pyxel.playm(3, loop=False)
        else:
            if self.is_on:
                self.offset = 2
            else:
                self.offset = 4


    def draw(self):
        pyxel.circ(self.posx, self.posy, self.radius, self.subcolor)
        pyxel.circ(self.posx, self.posy-self.offset, self.radius, self.color)

        if self.is_on: txt_color = 8
        else: txt_color = 7
        if self.textCenter:
            pyxel.text(align_text(self.posx, self.text), self.posy-self.offset-2, self.text, txt_color)
        else:
            pyxel.text(align_text(self.posx, self.text), self.posy+self.radius+3, self.text, txt_color)

class RectButton(Button):
    def __init__(self, x, y, text, w, h):
        super().__init__(x, y, text)
        self.width = w
        self.height = h
        self.color = 12
        self.subcolor = 5
        
    def update(self):

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  col_mouse_bt(pyxel.mouse_x, pyxel.mouse_y, self.posx, self.posy, self.width, self.height):
            self.offset = 0
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  col_mouse_bt(pyxel.mouse_x, pyxel.mouse_y, self.posx, self.posy, self.width, self.height):
            if self.is_on:
                self.is_on = False
                self.offset = 4
            else:
                self.is_on = True
                self.offset = 2
        else:
            if self.is_on:
                self.offset = 2
            else:
                self.offset = 4
        

    def draw(self):
        pyxel.rect(self.posx-(self.width/2)-self.offset, self.posy-(self.height/2)-self.offset, self.width+self.offset, self.height+self.offset, self.subcolor)
        pyxel.rect(self.posx-(self.width/2)-self.offset, self.posy-(self.height/2)-self.offset, self.width, self.height, self.color)

        if self.is_on: txt_color = 8
        else: txt_color = 7

        pyxel.text(align_text(self.posx, self.text)-self.offset, self.posy-self.offset-2, self.text, txt_color)

# Botão de ativação única, (ou seja, não é do tipo 'toggle')
class PushButton(Button):
    def __init__(self, x, y, text, r, textCenter=False):
        super().__init__(x, y, text)
        self.color = 12
        self.subcolor = 5
        self.radius = r
        self.offset = 2
        self.textCenter = textCenter
        
    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        bpos = [self.posx, self.posy]

        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 0
        elif pyxel.btnr(pyxel.MOUSE_LEFT_BUTTON) and  (dist(mouse_pos, bpos) < self.radius):
            self.offset = 2
            pyxel.playm(3, loop=False)
            return True
        else:
            self.offset = 2

    def draw(self):
        pyxel.circ(self.posx, self.posy, self.radius, self.subcolor)
        pyxel.circ(self.posx, self.posy-self.offset, self.radius, self.color)
        
        if self.textCenter:
            pyxel.text(align_text(self.posx, self.text), self.posy-self.offset-2, self.text, 7)
        else:
            pyxel.text(align_text(self.posx, self.text), self.posy+self.radius+3, self.text, 7)
