
def _find_val(sequence):
    num = 0

    for index in range(0, len(sequence)):
	num = num + (sequence[index] * ((-2) ** index))

    return num

def _convert_to_base(num):
    res = []

    while num != 0:
	remainder = abs(num % (-2))
	num = num / (-2)
	res.append(remainder)

    return res

def solution(A):
    return _convert_to_base(_find_val(A))

if __name__ == '__main__':
    
    '''
    print find_val(convert_to_base(num = 9))
    print find_val(convert_to_base(num = -9))
    print find_val(convert_to_base(num = -23))
    print find_val(convert_to_base(num = 23))
    '''
    print solution(A = [])

    print solution(A = [1, 0, 0, 1, 1])
    print solution(A = [1, 0, 0, 1, 1, 1])

    print solution(A = [1, 1, 0, 1])
    print solution(A = [1, 1, 0, 1, 0, 1, 1])
    
    all_correct = True
    for num in range(0, 10000):
	A = _convert_to_base(num = (-1) * num) # this is the sequence for +num
	
	if not _find_val(solution(A)) == (-1) * num:
	    print 'incorrect for {}'.format(num)
	    all_correct = False
    print 'Is All Correct? {}'.format(all_correct)