import test

def find_even_index(arr):
    res_index = 0
    sumleft = 0 # there are no elements to the left initially
    sumright = sum(arr[res_index + 1:])

    while True:
	if sumleft == sumright: return res_index
	# increment index and add to sumleft and sumright
	res_index = res_index + 1
	if res_index >= len(arr): break

	sumleft = sumleft + arr[res_index - 1]
	sumright = sumright - arr[res_index]

    # no such index found
    return -1

test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
test.assert_equals(find_even_index(range(1,100)),-1)
test.assert_equals(find_even_index([0,0,0,0,0]),0)
test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
test.assert_equals(find_even_index(range(-100,-1)),-1)