import os
from cryptography.fernet import Fernet
files = list()



for i in os.listdir():
    if i=="encryptor.py" or i == "decryptor.py" or i== "key1.key":
        continue
    if os.path.isfile(i):
        files.append(i)


with open("key1.key","rb") as key1:
    firstkey = key1.read()


for i in files:
    with open(i,"rb") as thefile:
        contents = thefile.read()
    decrypting = Fernet(firstkey).decrypt(contents)
    with open(i,"wb") as tf:
        tf.write(decrypting)
print("Decryption done!")