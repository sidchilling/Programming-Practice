# Check whther array A is a permutation

def solution(A):
    track_l = [False] * len(A)

    for num in A:
	if (num - 1) < len(A):
	    if track_l[num - 1]:
		# this element already occurred - not a permutation
		return 0
	    else:
		track_l[num - 1] = True

    # all the elements in track_l must be true
    for present in track_l:
	if not present:
	    # not a permutation
	    return 0

    # it is a permutation
    return 1

if __name__ == '__main__':
    print solution(A = [4, 1, 3, 2])
    print solution(A = [4, 1, 3])