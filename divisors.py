import test

def divisors(integer):
    res = []

    for i in range(2, integer):
	if integer % i == 0:
	    res.append(i)
    
    if len(res) > 0:
	return res
    else:
	return '{} is prime'.format(integer)

test.assert_equals(divisors(15), [3, 5])
test.assert_equals(divisors(12), [2, 3, 4, 6])
test.assert_equals(divisors(13), '13 is prime')