
def solution(A):
    left_sum = 0
    right_sum = sum(A)

    for i in range(len(A)):
	right_sum = right_sum - A[i]
	
	if right_sum == left_sum:
	    return i

	left_sum = left_sum + A[i]

    return -1

if __name__ == '__main__':
    print solution(A = [-1, 3, -4, 5, 1, -6, 2, 1])
