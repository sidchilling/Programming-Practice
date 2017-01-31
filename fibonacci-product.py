import test

def productFib(prod):
    prev = 0
    current = 1

    while True:
	if (prev * current) == prod: return [prev, current, True]
	if (prev * current) > prod: return [prev, current, False]
	prev, current = current, prev + current

test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])
	