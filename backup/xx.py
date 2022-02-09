def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

if 1 == 1:
    key = 'Merijn118'
    msg = "b'pqMJyoXsVWfluRSO4S19QUmsskbendlnn_W3o_nEsSE='"
    encrypted = encrypt(key, msg)
    decrypted = decrypt(key, encrypted)
    
    print('Message:', repr(msg))
    print('Key:', repr(key))
    print('Encrypted:', repr(encrypted))
    print('Decrypted:', repr(decrypted))
else :
  print("WTF")