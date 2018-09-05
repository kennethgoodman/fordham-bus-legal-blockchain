from ecdsa import SigningKey, SECP256k1
import hashlib
from hashlib import sha256
from utilitybelt import change_charset
from binascii import hexlify, unhexlify

def get_pair():
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()  # curve.generator * sk.privkey.secret_multiplier
    point = vk.pubkey.point
    pk_even_odd = point._Point__y % 2
    beginning_byte = {0:'02', 1:'03'}[pk_even_odd]
    return sk, beginning_byte + str(point._Point__x)


# PK -> address
# https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses#How_to_create_Bitcoin_Address
HEX_KEYSPACE = "0123456789abcdef"
B58_KEYSPACE = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
def pk_to_address(pk, version_byte = 0, num_leading_zeros=1):  # 0 for main net
	step_1 = pk
	pk = unhexlify(step_1)
	step_2 = sha256(pk)  # hexdigest to get hex
	step_3 = hashlib.new('ripemd160', step_2.digest())
	step_4 = '00' + step_3.hexdigest()  # if main net, num_leading_zeros
	step_5 = sha256(unhexlify(step_4))
	step_6 = sha256(step_5.digest())
	step_7 = checksum = step_6.hexdigest()[:8] # first 4 bytes
	step_8 = step_4 + checksum
	b58_s = change_charset(step_8, HEX_KEYSPACE, B58_KEYSPACE) # pybitcoin lib
	return B58_KEYSPACE[0] * num_leading_zeros + b58_s

while True:
    input("press any key and enter to generate again: ")
    while True:
        try:
            sk, pk = get_pair()
            addr = pk_to_address(pk)
            print("Secret Key = {}".format(sk.privkey.secret_multiplier))
            print("Public Key = {}".format(pk))
            print("Address    = {}".format(addr))
            break
        except:
            pass  # there is an error with odd length public key, instead of fixing by padding, just generate a new on

