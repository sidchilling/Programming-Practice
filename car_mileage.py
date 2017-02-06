import test

def palindrome(number):
    number = '{}'.format(number)
    return True if number == number[::-1] else False

def same_digits(number):
    number = '{}'.format(number)
    first_digit = number[0]
    for letter in number:
	if letter != first_digit: return False
    return True

def digit_followed_by_zeros(number):
    number = '{}'.format(number)
    if number[0] != '0' and int(number[1:]) == 0:
	return True
    return False

def _current_is_less(num1, num2):
    num1 = int(num1)
    next_num = num1 + 1
    if num1 == 9: next_num = 0
    if '{}'.format(next_num) == num2: return True
    return False

def incrementing_digits(number):
    number = '{}'.format(number)
    for index in range(0, len(number) - 1):
	if not _current_is_less(number[index], number[index + 1]): return False
    return True

def _current_is_more(num1, num2):
    num1 = int(num1)
    next_num = num1 - 1
    if '{}'.format(next_num) == num2: return True
    return False

def decrementing_digits(number):
    number = '{}'.format(number)
    for index in range(0, len(number) - 1):
	if not _current_is_more(number[index], number[index + 1]): return False
    return True

def is_interesting(number, awesome_phrases):
    # Return 2 (interesting), 1 (if an interesting number is within next two miles),
    # 0 (otherwise)

    if number <= 97: return 0 # 2 digit numbers cannot be interesting
    
    funcs = [
	digit_followed_by_zeros,
	same_digits,
	incrementing_digits,
	decrementing_digits,
	palindrome
    ]
    if number >= 100:
	# First, check if the number itself is interesting
	if number in awesome_phrases: return 2
	for func in funcs:
	    if func(number): return 2 # the number is interesting

    # Second, check if an interesting number is within 2 miles 
    numbers = [number + 1, number + 2]
    for number in numbers:
	if number in awesome_phrases: return 1
	for func in funcs:
	    if func(number): return 1
    # Third, Return 0
    return 0

phrases = [1337, 256]
tests = [
    {'n' : 3, 'res' : 0},
    {'n' : 1336, 'res' : 1},
    {'n' : 1337, 'res' : 2},
    {'n' : 11208, 'res' : 0},
    {'n' : 11209, 'res' : 1},
    {'n' : 11211, 'res' : 2}
]
for t in tests:
    test.assert_equals(is_interesting(t['n'], phrases), t['res'])