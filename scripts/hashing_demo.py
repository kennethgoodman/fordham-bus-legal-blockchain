from hashlib import sha256
from base64 import b64encode
import time

def sha(string):
    hashing_str = string.encode()
    hash_obj = sha256(hashing_str)
    digest = hash_obj.digest()
    b64_encoded = b64encode(digest)
    str_b64_encoded = b64_encoded.decode()
    return str_b64_encoded

while True:
    b = input("What should we hash? ")
    print('hash of "{}" is: {}'.format(b, sha(str(b))))
