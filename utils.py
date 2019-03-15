# -*-coding:Utf-8 -*

"""This file will contains functions and/or class/vars"""
import pickle
import os, re
import time
import inspect

from bot import *
from map import *
# Functions -----------------------------------------------------------------------------
cls = lambda:os.system('cls' if os.name=='nt' else 'clear')
def sleep(time_imp):
    try:
        time_imp = float(time_imp)
    except ValueError:
        print('Entrez un nombre s\'il vous plaît.\n')
    else:
        time.sleep(time_imp)
def wait(var="\n\n"):
    print(var)
    os.system("pause")

def save_data(file_name, datas, default, method="w"):
    if(len(method) > 1):
        with open(file_name, method) as obj:
            pickle.dump(datas, obj)
    else:
        with open(file_name, method) as obj:
            obj.write(datas)

def get_data(file, defaultValue, method="rb"):
    returnVar = ""
    if(len(method) > 1):
        try:
            if os.path.getsize(file) > 0:
                with open(file, method) as f:
                    returnVar = pickle.load(f)
        except FileNotFoundError:
            with open(file, "wb") as obj:
                pickl = pickle.Pickler(obj)
                pickl.dump(defaultValue)
                returnVar = defaultValue
    else:
        try:
            with open(file, method) as obj:
                returnVar = obj.read()
        except FileNotFoundError:
            with open(file, "w") as obj:
                obj.write(defaultValue)
                returnVar = defaultValue
    print(returnVar)
    return returnVar
def save_bot_position(bot, pos, method="ab"):
    if isinstance(bot, Bot):
        bot.set_position(pos)
        save_data(name_file_save, bot.get_datas(), dict(), method)

def get_current_games():
    l = dict()
    for obj in get_data(name_file_save, dict(), "rb"):
        l.dump(obj)
    return l

#Global Variables ------------------------------------------------------------------------


bot_char = 'X'
wall_char = 'O'
door_char = '.'
close_door_char = '-'
key_char = '¬'
list_letter_input = ['e','n','s','w','q'] #e = east; n = north; s = south; w = west; q = quit
name_file_save = "current_games"
if __name__ == "__main__":
    var = get_current_games()
    print(var)
    bot = Bot(3, 3, "Dave")
    bot2 = Bot(3, 2, "John")
    print(bot)
    print(bot2)
    save_bot_position(bot,(4,3),"wb")
    save_bot_position(bot2, (5,3),"wb")
    var = get_current_games()
    print(var)
    print(bot)
    print(bot2)
    wait()
