# Min number of jumps required by the frog

def solution(X, Y, D):
    diff = Y - X
    num_jumps = diff / D
    if diff % D != 0:
	num_jumps = num_jumps + 1
    return num_jumps

if __name__ == '__main__':
    print solution(X = 10, Y = 85, D = 30)
    print solution(X = 2, Y = 5, D = 2)
    print solution(X = 2, Y = 9, D = 3)
    print solution(X = 2, Y = 10, D = 3)
    print solution(X = 2, Y = 11, D = 3)