import pyxel

#Local Imports
from state_handler import change_state
import globals
import database
import queries

class Game:
    def __init__(self):
        # teste = queries.change_room(1)
        # print(teste.dados_sala.terreno)
        pyxel.init(globals.WIDTH, globals.HEIGHT, title="Project Nuclear", fps=30)
        pyxel.mouse(True)
        pyxel.load("assets.pyxres")
        
        pyxel.run(self.update, self.draw)

    def update(self):
        globals.current_state.update()

        change_state()

    def draw(self):
        globals.current_state.draw()        

Game()