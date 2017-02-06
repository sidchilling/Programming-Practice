import test

def _get_adjacent_nums(num):
    d = {
	'1' : ['1', '2', '4'],
	'2' : ['2', '1', '3', '5'],
	'3' : ['3', '2', '6'],
	'4' : ['4', '1', '5', '7'],
	'5' : ['5', '2', '8', '4', '6'],
	'6' : ['6', '3', '5', '9'],
	'7' : ['7', '4', '8'],
	'8' : ['8', '5', '0', '7', '9'],
	'9' : ['9', '6', '8'],
	'0' : ['0', '8']
    }

    return d.get(num, [])

def get_pins(observed):
    if len(observed) == 0: return []
    elif len(observed) == 1: return _get_adjacent_nums(num = observed[0])
    else:
	# more than one character
	res = []
	for possible in _get_adjacent_nums(observed[0]):
	    subpins = get_pins(observed = observed[1: len(observed)])
	    for subpin in subpins:
		res.append('{}{}'.format(possible, subpin))
	return res

print get_pins('1')
print get_pins('8')
print get_pins('11')
print get_pins('1357')