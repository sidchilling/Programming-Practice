
def min_unfairness(N, K, lists):
    lists = sorted(lists)
    start_pos = 0
    end_pos = start_pos + K - 1
    
    unfairness = lists[end_pos] - lists[start_pos]
    
    while end_pos < len(lists):
	current_unfairness = lists[end_pos] - lists[start_pos]
	if current_unfairness < unfairness:
	    unfairness = current_unfairness
	start_pos += 1
	end_pos += 1

    return unfairness

if __name__ == '__main__':
    print min_unfairness(N = 7, K = 3,
			lists = [10, 100, 300, 200, 1000, 20, 30])
    print min_unfairness(N = 10, K = 4,
    			lists = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200])
    print min_unfairness(N = 6, K = 3,
    			lists = [10, 20, 30, 100, 101, 102])