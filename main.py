from cryptography.fernet import Fernet
import os, platform, time, delt

time.sleep(1)

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

# Getting the decrypted key, then string -> bytes
decrykey = decrypt(pword, encrykey).encode('UTF-8')

# Using the decrypted key
fernet = Fernet(decrykey)

# Deleting all info about this/these variabel('s) after using
pword = "Nil"
decrykey = "Nil"
encrykey = "Nil"
del pword
del decrykey
del encrykey

# Opening and saving/reading the text
with open('info.csv', 'rb') as enc_file:
  encryfile = enc_file.read()

print(encryfile)

# Decrypting the text
decryfile = fernet.decrypt(encryfile)

print(decryfile)

# Deleting all info about this/these variabel('s) after using
encryfile = "Nil"
del encryfile 

# Creating/Opening a new file
# Writing the decrypted data to the file
with open('info.csv', 'wb') as dec_file:
  dec_file.write(decryfile)

decryfile = "Nil"
del decryfile

#system = platform.system()
#if system.lower() == "linux":
#    clear = lambda: os.system('clear')
#else:
#    clear = lambda: os.system('cls')

while True :
  time.sleep(1)
  print(">> Type something to encrypt")
  text = input("> ")
  if text.lower() == "!stop" :
    with open('info.csv', 'r') as infofile:
      file = infofile.read()
    print(file)
    chatlist = file.split()
    
    print(chatlist)

    with open('info.csv', 'w') as infofile:
      infofile.write(chatlist)
    
    with open('info.csv', 'rb') as infofile:
      file = infofile.read()
    
    encryfile = fernet.encrypt(file)

    with open('info.csv', 'wb') as infofile:
      infofile.write(encryfile)
      
    fernet = "Nil"
    del fernet
    exit()
  if text.lower() == "!check" :
    with open('info.csv', 'rb') as infofile:
      file = infofile.read()
    chatlist = file.split("\n")
    
    print(chatlist)
    chatlist = "Nil"
  else :
    with open('info.csv', 'rb') as infofile:
      file = infofile.read()
      
    chatlist = file.split("\n")
    chatlist.append(text)

    with open('info.csv', 'wb') as infofile:
      text = "\n".join(chatlist)
      infofile.write(text)

    chatlist = "Nil"
    
    print("original string: ", text)

    encText = fernet.encrypt(text.encode())
    print("encrypted string: ", encText)
 
    decText = fernet.decrypt(encText).decode()
    print("decrypted string: ", decText)
