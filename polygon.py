import sys

def _is_square(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and sides[3] > 0:
	if sides[0] == sides[1] == sides[2] == sides[3]:
	    return True
    return False

def _is_rectangle(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and sides[3] > 0:
	if sides[0] == sides[2] and sides[1] == sides[3]:
	    return True
    return False

if __name__ == '__main__':
    num_squares = 0
    num_rectangles = 0
    num_other_polygons = 0

    while True:
	try:
	    input_line = raw_input()
	except:
	    break
	sides = input_line.split(' ')
	try:
	    sides = [int(side) for side in sides]
	    if _is_square(sides):
		num_squares = num_squares + 1
	    elif _is_rectangle(sides):
		num_rectangles = num_rectangles + 1
	    else:
		num_other_polygons = num_other_polygons + 1
	except:
	    # Invalid input - Do nothing
	    continue
    
    print '{} {} {}'.format(num_squares, num_rectangles, num_other_polygons)