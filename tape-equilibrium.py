# Find the equilibrium of an array

def solution(A):
    min_eq = 1000000 # some large number

    sumleft = 0
    sumright = sum(A)

    for index in range(1, len(A)):
	val = A[index - 1]
	sumleft = sumleft + val
	sumright = sumright - val

	diff = abs(sumleft - sumright)

	min_eq = min(min_eq, diff)
    
    return min_eq

if __name__ == '__main__':
    print solution(A = [1, -1])
    print solution(A = [3, 1, 2, 4, 3])