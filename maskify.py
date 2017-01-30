import test

def maskify(cc):
    if len(cc) < 4: return cc
    return '{}{}'.format('#' * (len(cc) - 4), cc[-4::])

test.assert_equals(maskify(cc = '4556364607935616'), '############5616')
test.assert_equals(maskify(cc = '64607935616'), '#######5616')
test.assert_equals(maskify(cc = '1'), '1')
test.assert_equals(maskify(cc = ''), '')
test.assert_equals(maskify(cc = 'Skippy'), '##ippy')
test.assert_equals(maskify(cc = 'Nananananananananananananananana Batman!'),
		   '####################################man!')