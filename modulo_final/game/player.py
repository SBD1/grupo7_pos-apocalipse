import pyxel

#Local Imports
from entity import Entity
import bullet

class Player(Entity):

    def __init__(self,
        id_player,
        vida,
        nivel,
        caracteristica,
        capacidade_carregamento,
        defesa,
        ataque,
        nome,
        x,
        y,
        furtividade,
        id_local,
        id_personagem
    ) -> None:
        super().__init__(id_personagem, vida, nivel, caracteristica, capacidade_carregamento, defesa, ataque, nome, x, y)
        self.id_player = id_player
        self.furtividade = furtividade
        self.id_local = id_local

    def update(self, room_directions):
        super().update()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.bullets.append(bullet.Bullet(self.x, self.y, pyxel.mouse_x, pyxel.mouse_y, 2))
            # print(self.bullets[-1].vec_x)
            # print(self.bullets[-1].vec_y)
            # print("click")

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W):
            self.dir = "up"
            self.move(room_directions)
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            self.dir = "down"
            self.move(room_directions)
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.dir = "left"
            self.move(room_directions)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.dir = "right"
            self.move(room_directions)

    def draw(self):
        player_draw_args = [self.x-4, self.y-4, 0, 40, 0, 8, 8, pyxel.COLOR_BLACK]
        pyxel.blt(*player_draw_args)

        for blt in self.bullets:
            blt.draw()

        # pyxel.pset(self.x, self.y, pyxel.COLOR_CYAN)
