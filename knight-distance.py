
def solution(A, B):
    A, B = abs(A), abs(B) # normalize
    if A < B:
	A, B = B, A

    if A > (2 * B):
	seven = 0
	eight = (A + 2 * B) / 4
	ten = (A - 2 * B + 1) / 4
    else:
	seven = (2 * B - A) / 3
	eight = (2 * A - B) / 3
	ten = 0

    A = A - (2 * eight + seven + 2 * ten)
    B = B - (eight + 2 * seven - ten)

    if (A, B) == (1, 0):
	if eight > 0:
	    A, B = 3, 1
	    eight = eight - 1
    if (A, B) == (2, 2):
	if eight > 0:
	    A, B = 3, 1
	    eight = eight - 1
	    seven = seven + 1

    manual_vals = [[0, 3, 2],
		   [2, None, 2],
		   [4]]
    num_turns = seven + eight + ten + manual_vals[B][A - B]

    if num_turns > 100000000: return -2
    else:
	return num_turns

if __name__ == '__main__':
    print solution(A = 4, B = 5)
    print solution(A = 1, B = 0)
