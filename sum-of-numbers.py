import test

def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))

test.assert_equals(get_sum(1, 0), 1)
test.assert_equals(get_sum(1, 2), 3)
test.assert_equals(get_sum(0, 1), 1)
test.assert_equals(get_sum(0, -1), -1)
test.assert_equals(get_sum(2, -1), 2)