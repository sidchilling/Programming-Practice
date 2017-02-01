import test

def scramble(s1, s2):
    freq_d = {}
    for letter in s1:
	if not freq_d.get(letter, None): freq_d[letter] = 1
	else:
	    freq_d[letter] = freq_d[letter] + 1
    
    for letter in s2:
	if not freq_d.get(letter, None): return False
	else:
	    freq_d[letter] = freq_d[letter] - 1
	    if freq_d[letter] < 0: return False
    
    return True

test.assert_equals(scramble('rkqodlw', 'world'), True)
test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
test.assert_equals(scramble('katas', 'steak'), False)
test.assert_equals(scramble('scriptjava', 'javascript'), True)
test.assert_equals(scramble('scriptingjava', 'javascript'), True)