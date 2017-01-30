
def old_solution(A, B, K):
    diff = B - A

    if diff == 0:
	# A and B are equal
	if A % K == 0: return 1
	else:
	    return 0
    else:
	num = diff / K
	if diff >= K:
	    if diff % K != 0:
		num = num + 1
	else:
	    if (A % K == 0): num = num + 1
	    if (B % K == 0): num = num + 1
	return num

def solution(A, B, K):
    res = 0
    num = A
    while num <= B:
	if num % K == 0:
	    res = res + 1
	    num = num + K
	else:
	    num = num + 1
    return res

if __name__ == '__main__':
    print solution(A = 6, B = 11, K = 2) # 3
    print solution(A = 4, B = 5, K = 2) # 1
    print solution(A = 6, B = 11, K = 3) # 2
    print solution(A = 5, B = 5, K = 3) # 0
    print solution(A = 5, B = 6, K = 5) # 1
    print solution(A = 4, B = 5, K = 5) # 1