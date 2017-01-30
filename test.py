
def assert_equals(val1, val2):
    res = False
    if type(val1) == type(val2) and val1 == val2:
	res = True

    print '{} : {}'.format(val1, res)