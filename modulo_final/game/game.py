import pyxel

#Local Imports
from state_handler import change_state
import globals
import database

class Game:
    def __init__(self):
        # testeCon = database.conecta_db()
        # database.conecta_db()
        # print(testeCon)
        # sql = 'select * from arma'
        # consulta = database.consultar_db(sql)
        # print(consulta)
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