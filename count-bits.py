import test

def countBits(n):
    res_num = 0

    bin_n = '{0:08b}'.format(n)
    for bit in bin_n:
	if bit == '1':
	    res_num = res_num + 1

    return res_num

test.assert_equals(countBits(0), 0)
test.assert_equals(countBits(4), 1)
test.assert_equals(countBits(7), 3)
test.assert_equals(countBits(9), 2)
test.assert_equals(countBits(10), 2)