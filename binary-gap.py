
def solution(N):
    # Find the binary represention and keep track of the longest binary gap

    max_gap = 0
    current_gap = 0
    start_one_reached = False
    end_one_reached = False

    while N > 0:
	if (N % 2) == 0:
	    # remainder is zero
	    if start_one_reached: 
		current_gap = current_gap + 1
	else:
	    # remainder is one
	    if not start_one_reached: start_one_reached = True
	    elif start_one_reached and not end_one_reached:
		end_one_reached = True
	
	if start_one_reached and end_one_reached:
	    # we have gotten a binary gap
	    if current_gap > max_gap: max_gap = current_gap
	    current_gap = 0
	    start_one_reached = True
	    end_one_reached = False
	
	N = N / 2

    return max_gap

if __name__ == '__main__':
    print 'N = 1041: {}'.format(solution(N = 1041))
    print 'N = 9: {}'.format(solution(N = 9))
    print 'N = 529: {}'.format(solution(N = 529))
    print 'N = 20: {}'.format(solution(N = 20))
    print 'N = 15: {}'.format(solution(N = 15))