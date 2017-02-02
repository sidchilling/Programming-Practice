import csv


def plaza_A():
    res = []

    units = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    floors = range(2, 10)

    for floor_num in floors:
	for unit in units:
	    res.append(['Current Resident',
		'{}{}'.format(floor_num, unit),
		'318 Main Street', 'San Francisco', 'CA',
		'94105'])
    
    return res

def plaza_B():
    res = []

    units = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    floors = range(2, 10)

    for floor_num in floors:
	for unit in units:
	    res.append(['Current Resident',
		'{}{}'.format(floor_num, unit),
		'333 Beale Street', 'San Francisco', 'CA',
		'94105'])
    return res

def tower_B():
    res = []

    plans = [
	{'floor_range' : range(1, 2), 'units' : ['A', 'B', 'C', 'D']},
	{'floor_range' : range(2, 3), 'units' : ['A', 'B', 'C', 'D', 'E']},
	{'floor_range' : range(2, 29), 'units' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']},
	{'floor_range' : range(29, 41), 'units' : ['A', 'B', 'C', 'D', 'E']},
	{'floor_range' : range(41, 43), 'units' : ['A', 'B', 'C', 'D']}
    ]

    for plan in plans:
	for floor_num in plan['floor_range']:
	    for unit in plan['units']:
		res.append(['Current Resident',
	     '{}{}'.format(floor_num, unit),
	     '201 Folson Street', 'San Francisco', 'CA',
	     '94105'])
    
    return res

def tower_A():
    res = []

    plans = [
	{'floor_range' : range(3, 26), 'units' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']},
	{'floor_range' : range(26, 36), 'units' : ['A', 'B', 'C', 'D', 'E']},
	{'floor_range' : range(36, 38), 'units' : ['A', 'B']}
    ]

    for plan in plans:
	for floor_num in plan['floor_range']:
	    for unit in plan['units']:
		res.append(['Current Resident',
	     '{}{}'.format(floor_num, unit),
	     '338 Main Street', 'San Francisco', 'CA',
	     '94015'])

    return res

if __name__ == '__main__':

    with open('new-omni-address.csv', 'w') as out_csvfile:
	writer = csv.writer(out_csvfile, delimiter = ',',
		    quotechar = '"', quoting = csv.QUOTE_ALL)
	with open('omni-address.csv', 'rb') as in_csvfile:
	    reader = csv.reader(in_csvfile, delimiter = ',',
			quotechar = '"')
	    num_rows = 0
	    for row in reader:
		num_rows = num_rows + 1
		writer.writerow(row)
	# now we will write Lumnia's
	funcs = [plaza_A, plaza_B, tower_B, tower_A]
	for func in funcs:
	    for row in func():
		num_rows = num_rows + 1
		writer.writerow(row)
    
    print 'Number of rows written: {}'.format(num_rows)