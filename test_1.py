from gmpy2 import popcount
from random import randint
import sys

print("A[16]\tB[16]\tDOUT[16]\tAWON")

for i in range(0, int(sys.argv[1])):

    a = randint(0, 2**16)
    b = randint(0, 2**16)

    A = hex(a)
    B = hex(b)
    flag = popcount(a) >= popcount(b)
    DOUT = A if flag else B
    AWON = 1 if flag else 0
    print(f"{A}\t{B}\t{DOUT}\t{AWON}")