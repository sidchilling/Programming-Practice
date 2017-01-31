import test

def _reverse_or_rotate(chunk):
    cubes_sum = 0
    for digit in chunk:
	cubes_sum = cubes_sum + (int(digit) ** 3)

    if cubes_sum % 2 == 0:
	return chunk[::-1] # reverse
    else:
	return '{}{}'.format(chunk[1 : len(chunk)], chunk[0])

def revrot(strng, sz):
    if sz <= 0 or sz > len(strng): return ''
    str_list = []

    num_letters = 0
    chunk = ''
    for digit in strng:
	chunk = '{}{}'.format(chunk, digit)
	num_letters = num_letters + 1
	if num_letters == sz:
	    str_list.append(_reverse_or_rotate(chunk))
	    num_letters = 0
	    chunk = ''
    
    return ''.join(str_list)

test.assert_equals(revrot('123456987654', 6), '234561876549')
test.assert_equals(revrot('123456987653', 6), '234561356789')
test.assert_equals(revrot('66443875', 4), '44668753')
test.assert_equals(revrot('66443875', 8), '64438756')
test.assert_equals(revrot('664438769', 8), '67834466')
test.assert_equals(revrot('123456779', 8), '23456771')
test.assert_equals(revrot('', 8), '')
test.assert_equals(revrot('', 0), '')
test.assert_equals(revrot('123456779', 0), '')
test.assert_equals(revrot('1234', 5), '')
test.assert_equals(revrot('733049910872815764', 5), '330479108928157')