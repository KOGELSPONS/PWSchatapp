from cryptography.fernet import Fernet
import re

# The setup of making your chatapp password
def passwordsetup():
    while True:
        print(">> Requirements: Lenght: 8, Number: Yes, Capital: Yes")
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

# Deleting all info about this/these variabel('s) after being used fort the last time
password = "Nil"
del password

# key generation + bytes -> string
bytekey = Fernet.generate_key()
decrykey = bytekey.decode('UTF-8')

# Deleting all info about this/these variabel('s) after being used fort the last time
bytekey = "Nil"
del bytekey

# using the generated key
fernet = Fernet(decrykey)

# Generating a encrypted key
encrykey = encrypter(pword, decrykey)

# Deleting all info about this/these variabel('s) after being used fort the last time
pword = "Nil"
del pword
decrykey = "Nil"
del decrykey

# string the key in a file
with open('file.key', 'w') as file:
  file.write(encrykey)

# Deleting all info about this/these variabel('s) after being used fort the last time
encrykey = 'Nil'
del encrykey

# opening the original file bytes to encrypt 
with open('app.py', 'rb') as file:
    original = file.read()
      
# encrypting the file bytes
encryfile = fernet.encrypt(original)

# Deleting all info about this/these variabel('s) after being used fort the last time
fernet = "Nil"
del fernet

# Deleting all info about this/these variabel('s) after being used fort the last time
original = "Nil"
del original
  
# opening the file in write mode and 
# writing the encrypted bytes 
with open('app.key', 'wb') as encrypted_file:
    encrypted_file.write(encryfile)

# Remove any information about this/these variable('s) on the memory
encryfile = "Nil"
del encryfile
