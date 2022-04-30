#Local Imports
import globals 
from states.menu import MenuState
from states.run import RunState
from states.inventory import InventoryState
from states.game_over import GameOverState

def change_state():
    """
    Muda os estados da aplicação
    """
    if globals.next_state != "":

        if globals.next_state == "menu":
            globals.current_state = MenuState()
        
        elif globals.next_state == "inventory":
            globals.current_state = InventoryState()

        elif globals.next_state == "run":
            globals.current_state = RunState()

        elif globals.next_state == "game_over":
            globals.current_state = GameOverState()

        globals.next_state = ""
