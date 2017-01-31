import test

def solution(number):
    res_sum = 0

    for num in range(1, number):
	if (num % 3 == 0) or (num % 5 == 0):
	    res_sum = res_sum + num
    
    return res_sum

test.assert_equals(solution(10), 23)