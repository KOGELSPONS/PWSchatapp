from cryptography.fernet import Fernet
import os
import platform

import firstsetup
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
  print(">> Type something to encrypt")
  text = input(">")
  if text.lower() == "!stop" :
    with open('info.csv', 'rb') as infofile:
      file = infofile.read()
    encryfile = fernet.encrypt(file)
    os.remove("info.csv")
    with open('info.csv', 'wb') as infofile:
      infofile.write(encryfile)
    fernet = "Nil"
    del fernet
    exit()
  if text.lower() == "!check" :
    with open('info.csv', 'r') as infofile:
      file = infofile.read()
    print(file)
  else :
    with open('info.csv', 'w') as infofile:
      infofile.write(text)
    encText = fernet.encrypt(text.encode())
 
    print("original string: ", text)
    print("encrypted string: ", encText)
 
    decText = fernet.decrypt(encText).decode()
 
    print("decrypted string: ", decText)



