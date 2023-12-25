from db import get_users, insert_product, get_products, del_product, insert_log
from auth import login
import os
from time import sleep
import sys
import runpy

def start_console_line():
    is_auth = True
    auth_iterator = 0
    while(is_auth):
        email = input("Please enter admin email: ")
        password = input("Please enter admin password: ")
        users = get_users()
        is_auth = login(users, email, password)
        if is_auth == True:
            auth_iterator+=1
            print("Incorrect email or password")
            if auth_iterator == 3:
                print("Goodbye!!!!")
                sleep(4)
                os.system('cls')
                return False
            print("You have " + str(3 - auth_iterator) + " attempts")
            sleep(4)
            os.system('cls')
        else:
            print("Good verification!")
            insert_log("cmd_verification")
            sleep(4)
            os.system('cls')
            return True
        
def menu(is_bot_started):
    print("!!!Hello it is telegram bot admin pannel!!!")
    print("Please enter number what you want to do.")
    if is_bot_started:
        print("1. Bot is working")
    else:
        print("1. Start bot")
    print("2. Add Product")
    print("3. Delete Product")
    print("4. Close App and stop bot")
    choose = input("Enter number: ")
    sleep(2.5)
    os.system('cls')
    if int(choose) == 4:
        sys.exit()
    return choose

def bot_start():
    print("Bot is started!!!!")
    print("To Close bot enter Ctrl + C")
    runpy.run_module(mod_name='bot')
    
def add_product():
    print("For add product you must enter some values!")
    name = input("Enter Name : ")
    print("Cost Can be Null")
    cost = int(input("Enter Cost :"))
    print(insert_product(name, cost))
    insert_log("cmd_add_product")
    return "end"

def delete_product():
    print("For delete product you must choose which product you will delete!!!!")
    print("To delete enter ID of Product")
    products = get_products()
    for product in products:
        print(f"ID : {product[0]} , Name: {product[1]}, Cost: {product[2]}")
    id = input("Enter ID : ")
    del_product(id)
    insert_log("cmd_delete_product")
    return "end"

