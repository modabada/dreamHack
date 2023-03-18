#!/usr/bin/python3
from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hashlib
import random

class Person(object):
    def __init__(self, p):
        self.p = p
        self.g = 2
        self.x = random.randint(2, self.p - 1) 
    
    def calc_key(self):
        self.k = pow(self.g, self.x, self.p)
        return self.k

    def set_shared_key(self, k):
        self.sk = pow(k, self.x, self.p)
        aes_key = hashlib.md5(str(self.sk).encode()).digest()
        self.cipher = AES.new(aes_key, AES.MODE_ECB)

    def encrypt(self, pt):
        return self.cipher.encrypt(pad(pt, 16)).hex()

    def decrypt(self, ct):
        return unpad(self.cipher.decrypt(bytes.fromhex(ct)), 16)

# flag = open("flag", "r").read().encode()
flag = 'DreamHack'.encode()
prime = getPrime(1024)
print(f"Prime: {hex(prime)}")
alice = Person(prime) 
bob = Person(prime) 
me = Person(prime)
me.x = 32 # any fixed number
me_k = me.calc_key()

alice_k = alice.calc_key()
my_bob_sk = alice_k # man in middle
print(f"Alice sends her key to Bob. Key: {hex(alice_k)}")
bob.set_shared_key(me_k)

bob_k = bob.calc_key()
my_alice_sk = bob_k # man in middle
print(f"Bob sends his key to Alice. Key: {hex(bob_k)}")
alice.set_shared_key(me_k)

print()
print("They are sharing the part of flag")
alice_encrypt = alice.encrypt(flag[:len(flag) // 2])
bob_encrypt = bob.encrypt(flag[len(flag) // 2:])
print(f"Alice: {alice_encrypt}")
print(f"Bob: {bob_encrypt}")

print()
print('decrypted data')
me.set_shared_key(my_bob_sk)
print('send alice to bob:', me.decrypt(alice_encrypt))
me.set_shared_key(my_alice_sk)
print('send bob to alice:', me.decrypt(bob_encrypt))
