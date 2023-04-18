#!/usr/bin/python3
from Crypto.Util.number import getStrongPrime, bytes_to_long, inverse, long_to_bytes

N = int(input('N: '))
e = 65537
FLAG = int(input('FLAG: '))

print('plz decrypt c` and type again result. then, i can get plain text')
print('c`: ', hex(FLAG * pow(2, e) % N)[2:])

mPrime = int(input('input decrypted number: '))

m = mPrime // 2
print('plain text is ', long_to_bytes(m))


'''
==: 합동식 표시
`: 역원

c = pow(m, e, n)
m = pow(c, d, n)

c" = c * pow(2, e)
m" = pow(c", d, n)
    pow(c, d) * pow(2, e * d) % n
    pow(c, d) * 2 % n

pow(2, e, d) mod d == 2?

d == e`(mod q(n))
e` = b = b * e == 1(mod n)
e * d = e * e` == 1(mod n)
간단히 말하면
e` 은 e 와 곱하면 1(mod n) 과 합동식이 성립하는 수인데(역원의 정의)
mod n 을 할 경우 나머지가 e` 이 나오는 수는 d다.
e * d mod n == 0
따라서 c` 을 만들 때 설정한 pow(2, e) 는 pow(2, e * d, n) 으로 변환, e*d mod n 가 소멸되어 해독시
pow(c`, d, n) = pow(c, d) * pow(2, e * d) % n = pow(c, d) * 2 % n = m * 2 
로 계산됨
이런식으로 암호문을 조작해 평문을 얻는 방법을 CCA, Chosen chiper text 공격이라고 함
'''