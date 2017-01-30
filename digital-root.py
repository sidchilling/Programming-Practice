import test

def _find_sum(n):
    n = '{}'.format(n)
    res = 0
    for digit in n:
	res = res + int(digit)
    return res

def digital_root(n):
    digit_sum = _find_sum(n = n)
    while len('{}'.format(digit_sum)) > 1:
	digit_sum = _find_sum(n = digit_sum)
    return digit_sum

if __name__ == '__main__':
    test.assert_equals(digital_root(16), 7)
    test.assert_equals(digital_root(942), 6)
    test.assert_equals(digital_root(132189), 6)
    test.assert_equals(digital_root(493193), 2)
    test.assert_equals(digital_root(9), 9)
    test.assert_equals(digital_root(10), 1)