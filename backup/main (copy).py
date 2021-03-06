import os
import platform
import re
import time
from cryptography.fernet import Fernet

import delt

# Decrypting the encrypted key using password after decrypt() is activated
def decrypt(key, encrykey):
    decrykey = []
    for i, c in enumerate(encrykey):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        decrykey.append(chr((enc_c - key_c) % 127))
    return ''.join(decrykey)

# Reading the key out of the file
with open('file.key', 'r') as file:
    encrykey = file.read()

def passwordsetup():
    while True:
        time.sleep(1)
        print(">> Requirements: Lenght: 8, Number: Yes, Capital: Yes")
        password = input('>> Unlock chatapp: ')
        if len(password) < 8: 
            print(">> Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print(">> Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print(">> Make sure your password has a capital letter in it")
        else:
          passwordsetup()

# Entering your password
pword = input('>> Unlock chatapp: ')

# Getting the decrypted key
decrykey = decrypt(pword, encrykey)

# Using the decrypted key
fernet = Fernet(decrykey)

# Deleting all info about this/these variabel('s) after using
pword = "Nil"
decrykey = "Nil"
del pword
del decrykey
encrykey = "Nil"
del encrykey

# Opening and saving/reading the text
with open('info.csv', 'rb') as enc_file:
  encryfile = enc_file.read()

# Decrypting the text
  decryfile = fernet.decrypt(encryfile)

# Deleting all info about this/these variabel('s) after using
encryfile = "Nil"
del encryfile

os.remove("info.csv") 

# Creating/Opening a new file
# Writing the decrypted data to the file
with open('info.csv', 'wb') as dec_file:
  dec_file.write(decryfile)

decryfile = "Nil"
del decryfile

system = platform.system()
if system.lower() == "linux":
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')

while True :
  time.sleep(1)
  print(">> Type something to encrypt")
  text = input("> ")
  if text.lower() == "!stop" :
    with open('info.csv', 'r') as infofile:
      file = infofile.read()
    chatlist = file.split("\n")
    
    encryfile = fernet.encrypt(chatlist)

    with open('info.csv', 'w') as infofile:
      # Just removing it, so if it would store anything it would be gone
      infofile.write("1010101010101010101")
      os.remove("info.csv")
      # Writing encrypted data
      infofile.write(encryfile)
      
    fernet = "Nil"
    del fernet
    exit()
  if text.lower() == "!check" :
    with open('info.csv', 'r') as infofile:
      file = infofile.read()
    chatlist = file.split("\n")
    
    print(chatlist)
    chatlist = "Nil"
  else :
    with open('info.csv', 'r') as infofile:
      file = infofile.read()
      
    chatlist = file.split("\n")
    chatlist.append(text)

    with open('info.csv', 'w') as infofile:
      text = "\n".join(chatlist)
      infofile.write(text)

    chatlist = "Nil"
    
    print("original string: ", text)

    encText = fernet.encrypt(text.encode())
    print("encrypted string: ", encText)
 
    decText = fernet.decrypt(encText).decode()
    print("decrypted string: ", decText)
