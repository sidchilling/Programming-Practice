
def _find_num(s, c):
    num = 0
    for letter in s:
	if letter == c:
	    num = num + 1
    return num

def solution(S):
    # start from the middle

    index = len(S) / 2
    num_open = _find_num(s = S[0 : index], c = '(')
    num_close = _find_num(s = S[index + 1 : len(S)], c = ')')
    while True:
	if num_open == num_close:
	    return index + 1
	elif num_open < num_close:
	    # increment index
	    index = index + 1
	    if S[index] == '(': num_open = num_open + 1
	    else:
		num_close = num_close - 1
	else:
	    # num_close < num_open
	    index = index - 1
	    if S[index] == ')': num_close = num_close + 1
	    else:
		num_open = num_open - 1

if __name__ == '__main__':
    print solution(S = '(())')
    print solution(S = '(())))(')
    print solution(S = '))')
    print solution(S = '()')