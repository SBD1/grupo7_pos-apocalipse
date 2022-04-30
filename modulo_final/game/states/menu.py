import pyxel

#Local Imports
import utils
import globals
import buttons
from states.gamestate import GameState


# Estado Inicial, Menu principal
class MenuState(GameState):
    def __init__(self) -> None:
        super().__init__()
        self.btStart = buttons.PushButton(globals.WIDTH/2, globals.HEIGHT/2-20, "INICIAR", 15, textCenter=True)

    def update(self):
        super().update()

        if self.btStart.update():
            globals.next_state = "run"

    def draw(self):
        super().draw()

        self.btStart.draw()

        title = 'PROJETO NUCLEAR'
        pyxel.text(utils.align_text(globals.WIDTH/2, title), 10, title, 7)
        pyxel.text(utils.align_text(globals.WIDTH/2, "APERTE 'E' PARA PEGAR UM ITEM"), 80, "APERTE 'E' PARA PEGAR UM ITEM", pyxel.COLOR_WHITE)
        pyxel.text(utils.align_text(globals.WIDTH/2, "APERTE 'q' PARA FECHAR E SALVAR"), 90, "APERTE 'q' PARA FECHAR E SALVAR", pyxel.COLOR_WHITE)
        pyxel.text(utils.align_text(globals.WIDTH/2, "CLIQUE DO MOUSE PARA ATIRAR"), 100, "CLIQUE DO MOUSE PARA ATIRAR", pyxel.COLOR_WHITE)
        pyxel.text(utils.align_text(globals.WIDTH/2, "WASD PARA MOVIMENTAR"), 110, "WASD PARA MOVIMENTAR", pyxel.COLOR_WHITE)
        pyxel.text(utils.align_text(globals.WIDTH/2, "O BAND-AID RECUPERA SUA VIDA"), 120, "O BAND-AID RECUPERA SUA VIDA", pyxel.COLOR_WHITE)
