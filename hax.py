#Made by Armor
#Import libraries
from weld import program, privacy
import pyperclip
import time
import os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Armor's DLL Injector | V1")
url = "https://discord.gg/yNxAaAQPsj"
#copies my discord to the clipboard
os.system('cls')
def agree():
    z=input("YOU AGREE THAT I AM NOT RESPONSIBLE FOR DAMAGES OR BANS(Y/n)").lower()
    if z=="y":
        print("Agreed")
        os.system('cls')
    elif z=="n":
        exit()
    elif z=="":
        print("Agreed")
        os.system('cls')
    else:
        print("Invalid Please go back")
        agree()
agree()
def copy_discord():
    pyperclip.copy(url)
def shut():
    print("Goodbye!")
    time.sleep(1)
    exit()
welcome = ("Hello! Welcome to PY dll injector!(Works on most processes) type \"help\" for help!")
print(welcome, end='')
time.sleep(.01)

ison = False
def ask():
    
    CMD=input("\n>>> ").lower()
    if (CMD == "help"):
        print(f"""
        CMD: exit | Exits the program...
        CMD: start| Starts the injection!
        CMD: disc | Copies discord to clipboard!
        CMD: xps  | takes you to https://xps.rf.gd
        -------------------------------------------
        Credits:
        Made by Armor#0690
        Discord: {url}

            """)
        ask()
    elif (CMD == "start"):
        print("Starting Injection!")
        dll=input("Input DLL name:")
        pid=int(input("Input PID here:"))
        program.attach(dll, pid)
    elif (CMD == "exit"):
        shut()
    elif (CMD == "disc"):
        copy_discord()
        ask()
    elif (CMD == "xps"):
        os.system("start https://xps.rf.gd")
        ask()
    elif (CMD == "chacha"):
        global ison
        if ison == False:
            ctypes.windll.kernel32.SetConsoleTitleW("Slide to the left! Slide to the right!")
            ison = True
        elif ison == True:
            ctypes.windll.kernel32.SetConsoleTitleW("Armor's DLL Injector | V1")
            ison = False
        os.system('cls')
        ask()
    else:
        print("Please choose from the help list!")
        ask()
ask()
