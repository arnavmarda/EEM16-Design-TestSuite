from gmpy2 import popcount
from random import randint
import sys

def tohex(val):
    if val >= 0:
        return hex(val)
    else:
        return hex(256 + val)

print("SIGN[7]\tD1[7]\tD0[7]\tDOUT[8]\tNAN[1]")

print("# EDGE CASES")
edgecases = [
    [43, 0, 0, 0, 0],
    [45, 0, 0, 0, 0],
    [45, 9, 9, -99, 0],
    [43, 9, 9, 99, 0],
]

for case in edgecases:
    SIGN = hex(case[0])
    D1 = hex(case[1]+48)
    D0 = hex(case[2]+48)
    TC = tohex(case[3])
    NAN = hex(case[4])
    print(f"{SIGN}\t{D1}\t{D0}\t{TC}\t{NAN}")

print("# CASES THAT SHOULD RETURN NAN=1")

for _ in range(0, 20):
    sign_val = randint(0, 42) if randint(0, 1) else randint(46, 128)
    d1 = randint(48, 57)
    d2 = randint(48, 57)

    SIGN = hex(sign_val)
    D1 = hex(d1)
    D0 = hex(d2)
    TC = 0xff
    NAN = hex(1)

    print(f"{SIGN}\t{D1}\t{D0}\t{TC}\t{NAN}")

for _ in range(0, 20):
    sign_val = 43 if randint(0, 1) else 45
    d1 = randint(0, 47) if randint(0, 1) else randint(58, 128)
    d2 = randint(0, 47) if randint(0, 1) else randint(58, 128)

    SIGN = hex(sign_val)
    D1 = hex(d1)
    D0 = hex(d2)
    TC = 0xff
    NAN = hex(1)

    print(f"{SIGN}\t{D1}\t{D0}\t{TC}\t{NAN}")

for _ in range(0, 20):
    sign_val = randint(0, 42) if randint(0, 1) else randint(46, 128)
    d1 = randint(0, 47) if randint(0, 1) else randint(58, 128)
    d2 = randint(0, 47) if randint(0, 1) else randint(58, 128)

    SIGN = hex(sign_val)
    D1 = hex(d1)
    D0 = hex(d2)
    TC = 0xff
    NAN = hex(1)

    print(f"{SIGN}\t{D1}\t{D0}\t{TC}\t{NAN}")

print("# VALID CASES")

for _ in range(0, int(sys.argv[1])):
    sign_val = 43 if randint(0, 1) else 45
    d1 = randint(48, 57)
    d2 = randint(48, 57)
    sign = 1 if sign_val == 43 else -1
    tc = ((d1-48)*10 + (d2-48)) * sign
    nan = 0

    SIGN = hex(sign_val)
    D1 = hex(d1)
    D0 = hex(d2)
    TC = tohex(tc)
    NAN = hex(nan)

    print(f"{SIGN}\t{D1}\t{D0}\t{TC}\t{NAN}")