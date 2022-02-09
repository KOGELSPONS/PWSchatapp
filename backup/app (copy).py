import socket
import select
import sys
import os
import platform
import time
from termcolor import colored, cprint
from replit import db

#cprint('Hello, World!', 'green', 'on_red')

active = True
system = platform.system()
if system.lower() == "linux":
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')
def startup():
  account = db["user"]
  if account: 
    cprint('>>> Application Started:', 'red', attrs=['underline', 'bold'])
    cprint('>> Enter your password:')
    pword = input('')

inpass = input('>')



while active:

    while True:
        message_local = input("")
        if message_local.lower() == "sos" or message_local.lower() == "s":
            print("clear")
            clear()
        else:
            print("hoi")
