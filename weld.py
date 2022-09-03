import sys
import os
import pyrasite
import signal
import psutil
import requests
import time
import random
import subprocess
from writer import Injector
injector = Injector()
def p_load():
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
class privacy:
    def watch(name, systemi):
        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                processName = proc.name()
                processID = proc.pid
                return processName , ' ::: ', processID
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
class program:
    def attach(dll, procid):
        leng = procid
        if (leng < 0):
            print("No Process ID Specified, try again")
            time.sleep(5)
            os.system('cls')
            exit()
        elif (leng > 99999):
            print("Invalid Process ID try again")
            time.sleep(5)
            os.system('cls')
        else:
            print("Attaching to program")
            p_load()
            injector.load_from_pid(procid)
            injector.inject_dll(dll)
            injector.unload()
            print("Injected!")
