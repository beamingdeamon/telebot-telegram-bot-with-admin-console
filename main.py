from console_line import start_console_line, menu, bot_start, add_product, delete_product
import sys
import os

is_go_to_next_step = start_console_line()
if(is_go_to_next_step == False) :
    sys.exit()
is_bot_started = False

while(True): 
    os.system('cls')
    menu_choose = menu(is_bot_started)
    if int(menu_choose) == 1:
        bot_start()
    elif int(menu_choose) == 2:
        add_product()
    elif int(menu_choose) == 3:
        delete_product()