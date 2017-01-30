
def solution(X, A):
    
    track_l = [False] * (X + 1)
    set_num_times = 0

    for second in range(0, len(A)):
	if not track_l[A[second]]:
	    # set
	    track_l[A[second]] = True
	    set_num_times = set_num_times + 1
	    if set_num_times == X:
		return second
    
    return -1

if __name__ == '__main__':
    print solution(X = 1, A = [1])
    print solution(X = 5, A = [1, 3, 1, 4, 2, 3, 5, 4])
    print solution(X = 4, A = [1, 2, 4, 2, 1, 4])