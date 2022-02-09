from cryptography.fernet import Fernet
import os

# Activates if existing
if os.path.exists("firstsetup.py") :
  # Used to create a password and encrypt your key with that password get's deleted after
  import firstsetup
elif not os.path.exists("system.key") or not os.path.exists("delt.key") or not os.path.exists("app.key") or not os.path.exists("data.key") :
  os.remove("app.key")
  os.remove("system.key")
  os.remove("delt.key")
  os.remove("data.key")
  print("Reinstal your OS")
  exit()

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

# Deleting all info about this/these variabel('s) after being used fort the last time
pword = "Nil"
decrykey = "Nil"
del pword
del decrykey
encrykey = "Nil"
del encrykey

# Opening and saving/reading the text
with open('app.key', 'rb') as enc_file:
  encryfile = enc_file.read()

# Decrypting the text
  decryfile = fernet.decrypt(encryfile)

# Deleting all info about this/these variabel('s) after being used fort the last time
fernet = "Nil"
del fernet
encryfile = "Nil"
del encryfile

# Creating/Opening a new file
# Writing the decrypted data to the file
with open('test.py', 'wb') as dec_file:
  dec_file.write(decryfile)

decryfile = "Nil"
del decryfile

