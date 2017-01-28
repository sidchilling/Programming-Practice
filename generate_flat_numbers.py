
def _two_digit(num):
    num = '{}'.format(num)
    if len(num) == 2:
	return num
    else:
	return '0{}'.format(num)

all_floor_plans = [
    {'floor_num_range' : range(4, 6), 'flat_num_range' : range(1, 14), 'flat_num_skip' : []},
    {'floor_num_range' : range(6, 8), 'flat_num_range' : range(1, 14), 'flat_num_skip' : [2, 3]},
    {'floor_num_range' : range(8, 9), 'flat_num_range' : range(1, 14), 'flat_num_skip' : [2, 3, 10]},
    {'floor_num_range' : range(9, 29), 'flat_num_range' : range(1, 14), 'flat_num_skip' : [2, 3, 4, 10]},
    {'floor_num_range' : range(29, 31), 'flat_num_range' : range(1, 14), 'flat_num_skip' : [2, 3, 4, 7, 10, 12]},
    {'floor_num_range' : range(31, 34), 'flat_num_range' : range(1, 14), 'flat_num_skip' : [2, 3, 4, 7, 10, 12]},
    {'floor_num_range' : range(34, 40), 'flat_num_range' : range(1, 14), 'flat_num_skip' : [2, 3, 4, 7, 8, 10, 12]},
    {'floor_num_range' : range(40, 41), 'flat_num_range' : range(1, 14), 'flat_num_skip' : [2, 3, 4, 7, 8, 10, 12]}
]

for floors_plan in all_floor_plans:
    for floor_num in floors_plan['floor_num_range']:
	for flat_num in floors_plan['flat_num_range']:
	    if flat_num not in floors_plan['flat_num_skip']:
		print '{}{}'.format(floor_num, _two_digit(flat_num))