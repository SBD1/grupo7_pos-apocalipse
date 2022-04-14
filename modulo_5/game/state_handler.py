import globals 
from states.menu import MenuState
from states.run import RunState

def change_state():
    """
    Muda os estados da aplicação
    """
    if globals.next_state != "":

        if globals.next_state == "menu":
            globals.current_state = MenuState()

        elif globals.next_state == "run":
            globals.current_state = RunState()

        globals.next_state = ""
