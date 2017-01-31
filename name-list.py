import test

def namelist(names):
    names = ['{}'.format(x['name']) for x in names]
    res = ', '.join(names)

    if res.rfind(',') != -1:
	res = '{} &{}'.format(res[0 : res.rfind(',')],
		      res[res.rfind(',') + 1:])
    
    return res

test.assert_equals(namelist([{'name' : 'Bart'}, {'name' : 'Lisa'}, {'name' : 'Maggie'}]),
		  'Bart, Lisa & Maggie')
test.assert_equals(namelist([{'name' : 'Bart'}, {'name' : 'Lisa'}]),
		  'Bart & Lisa')
test.assert_equals(namelist([{'name' : 'Bart'}]), 'Bart')
test.assert_equals(namelist([]), '')