# Find missing element from array

def solution(A):

    l = [False] * (len(A) + 1)
    for index in range(0, len(A)):
	l[A[index] - 1] = True
    for i in range(0, len(l)):
	if not l[i]:
	    return i + 1

if __name__ == '__main__':
    print solution(A = [2, 3, 1, 5])
