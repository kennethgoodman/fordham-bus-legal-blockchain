from hashlib import sha256
from base64 import b64encode
import time

def sha(string):
    temp = str(time.time())
    hashing_str = (string + temp).encode()
    hash_obj = sha256(hashing_str)
    digest = hash_obj.digest()
    b64_encoded = b64encode(digest)
    str_b64_encoded = b64_encoded.decode()
    return str_b64_encoded

def while_not_begins(beginning):
    i = 0
    x = sha(str(i))
    while not x.lower().startswith(beginning.lower()):
        print(i, x)
        i += 1
        x = sha(str(i))
    print(i, x)

while True:
    b = input("What is the beginning?")
    while_not_begins(b)
