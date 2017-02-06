import test

from decimal import Decimal

def v(k, n):
    return 1 / Decimal(k * ((n + 1) ** (2 *k)))

def u(k, N):
    res = 0
    for n in range(1, N + 1):
	res = res + v(k, n)
    return res

def doubles(maxk, maxn):
    res = 0
    for k in range(1, maxk + 1):
	res = res + u(k, maxn)
    return float(res)

print doubles(1, 3)
print doubles(1, 10)
print doubles(10, 100)
print doubles(10, 1000)
print doubles(10, 10000)
print doubles(20, 10000)