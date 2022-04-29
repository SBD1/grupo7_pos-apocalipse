import pyxel

#Local Imports
import utils
import globals

# Classe Entidade abstrata, pai para o player, para os npcs e inimigos
class Entity:
    def __init__(self,
        id,
        vida,
        nivel,
        caracteristica,
        capacidade_carregamento,
        defesa,
        ataque,
        name,
        x,
        y) -> None:
        self.id = id
        self.vida = vida
        self.nivel = nivel
        self.caracteristica = caracteristica
        self.capacidade_carregamento = capacidade_carregamento
        self.defesa = defesa
        self.ataque = ataque
        self.x = x
        self.y = y
        self.name = name
        self.speed = 2
        self.dir = ""
        self.bullets = []
        self.health = 120
        self.total_health = 120

    def update(self):
        self.dir = ""

        for b in self.bullets:
            b.update()

        if(self.bullets != []):
            if(self.bullets[0].time <= 0):
                del self.bullets[0]

    def move(self, room_directions = {}):
        old_pos = [self.x, self.y]
        reset_pos = False

        if self.dir == "up":
            self.y -= self.speed
        elif self.dir == "down":
            self.y += self.speed
        elif self.dir == "left":
            self.x -= self.speed
        elif self.dir == "right":
            self.x += self.speed

        col_type = utils.col_map(self.x, self.y)

        if(self.__class__.__name__ == "Player" and col_type >=2 and col_type <= 5):
            new_room_id = room_directions[self.get_door_direction(col_type)]
            globals.next_room = new_room_id

            if new_room_id != 0:
                self.enter_door(col_type)
            else:
                reset_pos = True
        elif(col_type >= 1):
            reset_pos = True

        if(reset_pos):
            self.x = old_pos[0]
            self.y = old_pos[1]

        return col_type

    def enter_door(self, dir_int):
        dir = utils.inv_dir(self.get_door_direction(dir_int))

        if dir == "right":  pos = utils.get_screen_pos(14, 7)
        elif dir == "left": pos = utils.get_screen_pos(1, 7)
        elif dir == "up":   pos = utils.get_screen_pos(8, 1)
        elif dir == "down": pos = utils.get_screen_pos(8, 12)

        self.x = pos[0]
        self.y = pos[1]

    def get_door_direction(self, dir_int):
        return self.get_direction(dir_int-2)

    def get_direction(self, dir_int):
        if(dir_int == 0): return "up"
        elif(dir_int == 1): return "down"
        elif(dir_int == 2): return "left"
        elif(dir_int == 3): return "right"
        else: return "null"

    def draw(self):
        # pyxel.pset(self.x, self.y,     pyxel.COLOR_RED)
        # for point in globals.collision_points:
        #     pyxel.pset(point[0]+self.x, point[1]+self.y, pyxel.COLOR_WHITE)

        for blt in self.bullets:
            blt.draw()
