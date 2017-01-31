import test

def Descending_Order(num):
    return int(''.join(map(str, sorted([int(digit) for digit in '{}'.format(num)],
				       reverse = True))))

test.assert_equals(Descending_Order(0), 0)
test.assert_equals(Descending_Order(15), 51)
test.assert_equals(Descending_Order(123456789), 987654321)