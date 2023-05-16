from Crypto.Util.number import getPrime, inverse, bytes_to_long, isPrime, long_to_bytes
from random import randrange, choices
from hashlib import sha1
import string


p = int(input('p: '))
q = int(input('q: '))
g = int(input('g: '))
y = int(input('y: '))
token = bytes(input('token: '), 'UTF-8')

m1 = bytes_to_long(b'firstTestMessage')
h1 = bytes_to_long(sha1(long_to_bytes(m1)).digest())
print('sign this')
print('m1:', hex(m1)[2:])
s1 = int(input('s1: '))

m2 = bytes_to_long(b'secondTestMessage')
h2 = bytes_to_long(sha1(long_to_bytes(m2)).digest())
print('sign this')
print('m2:', hex(m2)[2:])
s2 = int(input('s2: '))

r = int(input('r: '))


# calc
k = ((h1 - h2) * inverse(s1 - s2, q)) % q
x = inverse(k, q)
h = bytes_to_long(sha1(token).digest())
s = inverse(k, q) * (h + x * r) % q

print('=' * 20)
print('x:', x)
print('answer')
print('msg(hex):', hex(bytes_to_long(token))[2:])
print('r: ', r)
print('s: ', s)

