import calcmodule
import intro

def init_sequence():

    calcmodule.get_input()
    calcmodule.seperate_nums()
    calcmodule.perform_calc()
    calcmodule.select_state()


intro.print_intro()
init_sequence()