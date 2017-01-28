# Find the unpaired element

def solution(A):
    d = {}

    for i in range(0, len(A)):
	if d.get('{}'.format(A[i]), None):
	    # element already encountered once
	    del d['{}'.format(A[i])]
	else:
	    d['{}'.format(A[i])] = 1
    
    return int(d.keys()[0])

if __name__ == '__main__':
    print solution(A = [1])
    print solution(A = [1, 1, 3])
    print solution(A = [1, 2, 3, 1, 2])
    print solution(A = [9, 3, 9, 3, 9, 7, 9])