
def solution(N, A):
    # N is the number of counters
    # A is the array of operations

    counters = [0] * N
    max_counter_value = 0

    for op_val in A:
	if op_val == (N + 1):
	    # set to the max value
	    counters = [max_counter_value] * N
	else:
	    # we have increment one specific counter
	    counters[op_val - 1] = counters[op_val - 1] + 1
	    max_counter_value = max(max_counter_value, counters[op_val - 1])
    
    return counters

if __name__ == '__main__':
    print solution(N = 5, A = [3, 4, 4, 6, 1, 4, 4])