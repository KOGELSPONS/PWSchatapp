from cryptography.fernet import Fernet
import time
import re

# The setup of making your chatapp password
def passwordsetup():
    while True:
        time.sleep(1)
        print(">> Requirements: Lenght 8, Number, Capital Letter")
        print(">> Enter your Password:")
        password = input("> ")
        if len(password) < 8: 
            print(">> Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print(">> Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print(">> Make sure your password has a capital letter in it")
        else:
            print(">> Retype your password:")
            retypepassword = input("> ")
            if retypepassword == password :
              retypepassword = "Nil"
              del retypepassword
              print(">> Password check complete")
              print(">>> Setting up Chatapp!")
              print(">>> This may take a while")
              return password
            elif retypepassword != password :
              retypepassword = "Nil"
              del retypepassword
              password = "Nil"
              del password
              print(">> Try agian!")
              passwordsetup()

# The encryption procces of the key using your password
def encrypter(pword, key):
    encrykey = []
    for i, c in enumerate(key):
        pword_c = ord(pword[i % len(pword)])
        enc_c = ord(c)
        encrykey.append(chr((enc_c + pword_c) % 127))
    return ''.join(encrykey)

pword = passwordsetup()

# Deleting all info about this/these variabel('s) after used
password = "Nil"
del password

# key generation + bytes -> string
bytekey = Fernet.generate_key()
print(bytekey)
decrykey = bytekey.decode('UTF-8')
print(decrykey)

# Deleting all info about this/these variabel('s) after used
bytekey = "Nil"
del bytekey

# using the generated key
fernet = Fernet(decrykey)

# Generating a encrypted key
encrykey = encrypter(pword, decrykey)

# Deleting all info about this/these variabel('s) after used
pword = "Nil"
del pword
decrykey = "Nil"
del decrykey

# Writing the encrypted key in a file
with open('file.key', 'w') as file:
  file.write(encrykey)

# Deleting all info about this/these variabel('s) after used
encrykey = 'Nil'
del encrykey

import delt

# opening the original file bytes to encrypt 
with open('info.csv', 'r') as file:
    original = file.read()
      
# encrypting the file bytes
encryfile = fernet.encrypt(original)

# Deleting all info about this/these variabel('s) after used
fernet = "Nil"
del fernet

# Deleting all info about this/these variabel('s) after used
original = "Nil"
del original
  
# opening the file in write mode and 
# writing the encrypted bytes 
with open('info.csv', 'w') as encrypted_file:
    encrypted_file.write(encryfile)

# Remove any information about this/these variable('s) on the memory
encryfile = "Nil"
del encryfile