import sys

def pairExist(numbers, target_sum):
    numbers = sorted(numbers)
    start = 0
    end = len(numbers) - 1

    while start < end:
	if numbers[start] + numbers[end] == target_sum:
	    return 1
	elif numbers[start] + numbers[end] < target_sum:
	    start = start + 1
	else:
	    end = end - 1
    return 0

if __name__ == '__main__':
    target_sum = int(raw_input())
    array_length = int(raw_input())

    numbers = []

    for i in range(0, array_length):
	numbers.append(int(raw_input()))

    print pairExist(numbers, target_sum)