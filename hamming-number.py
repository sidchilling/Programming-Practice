import test

def hamming(n):
    h = [1] * n
    x2, x3, x5 = 2, 3, 5
    i = j = k = 0

    for index in range(1, n):
	h[index] = min(x2, x3, x5)
	if x2 == h[index]:
	    i = i + 1
	    x2 = 2 * h[i]
	if x3 == h[index]:
	    j = j + 1
	    x3 = 3 * h[j]
	if x5 == h[index]:
	    k = k + 1
	    x5 = 5 * h[k]
    
    return h[-1]

test.assert_equals(hamming(1), 1)
test.assert_equals(hamming(2), 2)
test.assert_equals(hamming(3), 3)
test.assert_equals(hamming(4), 4)
test.assert_equals(hamming(5), 5)
test.assert_equals(hamming(6), 6)
test.assert_equals(hamming(7), 8)
test.assert_equals(hamming(8), 9)
test.assert_equals(hamming(9), 10)
test.assert_equals(hamming(10), 12)
test.assert_equals(hamming(11), 15)
test.assert_equals(hamming(12), 16)
test.assert_equals(hamming(13), 18)
test.assert_equals(hamming(14), 20)
test.assert_equals(hamming(15), 24)
test.assert_equals(hamming(16), 25)
test.assert_equals(hamming(17), 27)
test.assert_equals(hamming(18), 30)
test.assert_equals(hamming(19), 32)
