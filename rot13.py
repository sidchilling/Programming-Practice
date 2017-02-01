import test

import string
from codecs import encode as _dont_use_this


def _get_rotated_index(c, letters):
    if letters.find(c) + 13 < len(letters):
	return letters.find(c) + 13
    else:
	return (letters.find(c) + 13) - len(letters)

def _get_rotate_char(char):
    if char in string.ascii_uppercase:
	# this is a upper-case letter
	return string.ascii_uppercase[_get_rotated_index(c = char,
						 letters = string.ascii_uppercase)]
    else:
	# this is a lower-case letter
	return string.ascii_lowercase[_get_rotated_index(c = char,
						 letters = string.ascii_lowercase)]

def rot13(message):
    res = ''

    for letter in message:
	if not letter.isalpha(): res = '{}{}'.format(res, letter)
	else:
	    res = '{}{}'.format(res, _get_rotate_char(char = letter))
    
    return res

test.assert_equals(rot13('test'), 'grfg')
test.assert_equals(rot13('Test'), 'Grfg')