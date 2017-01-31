import test

def iq_test(numbers):
    numbers = numbers.split(' ')
    evens = []
    odds = []

    for index in range(0, len(numbers)):
	if int(numbers[index]) % 2 == 0:
	    # even
	    evens.append(index + 1)
	else:
	    odds.append(index + 1)
    
    if len(evens) == 1: return evens[0]
    else: return odds[0]

test.assert_equals(iq_test('2 4 7 8 10'), 3)
test.assert_equals(iq_test('1 2 2'), 1)
test.assert_equals(iq_test('1 2 1 1'), 2)