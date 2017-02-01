import test
import math

def isPP(n):
    for m in range(2, int(math.sqrt(n)) + 1):
	k = int(round(math.log(n, m)))
	if m ** k == n:
	    return [m, k]
    return None

test.assert_equals(isPP(4), [2, 2])
test.assert_equals(isPP(9), [3, 2])
test.assert_equals(isPP(5), None)

ns = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128,
      144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400,
      441, 484]
for n in ns:
    print 'n = {}, {}'.format(n, isPP(n))