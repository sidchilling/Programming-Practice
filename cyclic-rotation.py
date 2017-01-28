# Rotate an array K-times
from operator import itemgetter

def _rotate(index, length, K):
    for times in range(0, K):
	index = index + 1
	if index == length:
	    index = 0
    return index

def solution(A, K):
    # the array A is to be rotated K times
    
    el_pos = []
    for arr_index in range(0, len(A)):
	el_pos.append({
	    'el' : A[arr_index],
	    'pos' : _rotate(index = arr_index, length = len(A), K = K)
	})
    el_pos = sorted(el_pos, key = itemgetter('pos'))
    return [el['el'] for el in el_pos]

if __name__ == '__main__':
    print solution(A = [], K = 100)
    print solution(A = [1], K = 50)
    print solution(A = [1, 2], K = 1)
    print solution(A = [1, 2, 3], K = 2)
    print solution(A = [1, 2, 3], K = 0)
    print solution(A = [3, 8, 9, 7, 6], K = 3)