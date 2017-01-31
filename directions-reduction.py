import test

def dirReduc(arr):

    opps = {
	'NORTH' : 'SOUTH',
	'SOUTH' : 'NORTH',
	'EAST' : 'WEST',
	'WEST' : 'EAST'
    }

    res_arr = []

    for direction in arr:
	if not res_arr: res_arr.append(direction)
	else:
	    if res_arr[len(res_arr) - 1] == opps.get(direction):
		res_arr.pop()
	    else:
		res_arr.append(direction)
    
    return res_arr

test.assert_equals(dirReduc(['NORTH', 'SOUTH', 'EAST', 'WEST']), [])
test.assert_equals(dirReduc(['NORTH', 'EAST', 'WEST', 'SOUTH', 'WEST', 'WEST']),
		  ['WEST', 'WEST'])
test.assert_equals(dirReduc(['NORTH', 'WEST', 'SOUTH', 'EAST']),
		  ['NORTH', 'WEST', 'SOUTH', 'EAST'])