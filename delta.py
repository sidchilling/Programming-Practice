import sys

if __name__ == '__main__':
    input_str = raw_input()

    numbers = input_str.split(' ')
    numbers = [int(num) for num in numbers]

    res = [numbers[0]]

    for index in range(1, len(numbers)):
	diff = numbers[index] - numbers[index - 1]
	if -127 <= diff <= 127:
	    res.append(diff)
	else:
	    res.append(-128)
	    res.append(diff)
    
    
    print ' '.join(map(str, res))