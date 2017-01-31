import test

def xo(s):
    return s.lower().count('x') == s.lower().count('o')

test.assert_equals(xo('xo'), True)
test.assert_equals(xo('xo0'), True)
test.assert_equals(xo('xxxoo'), False)