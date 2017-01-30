# Find the minimal positive missing integer from an array

def solution(A):
    track_l = [False] * len(A)

    for num in A:
	if num > 0:
	    # we are interested in this element
	    if (num - 1) < len(track_l):
		track_l[num - 1] = True

    for index in range(0, len(track_l)):
	if not track_l[index]:
	    return index + 1

    return len(track_l) + 1

if __name__ == '__main__':
    print solution(A = [5])
    print solution(A = [1, 3, 6, 4, 1, 2])