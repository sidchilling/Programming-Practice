import test

def calc(expr):
    expr = expr.strip()
    if len(expr) == 0: return 0
    expr = expr.split(' ')

    stack = []
    
    for letter in expr:
	if letter in ['+', '-', '*', '/']:
	    # operation
	    op1 = stack.pop()
	    op2 = stack.pop()
	    if letter == '+':
		stack.append(op2 + op1)
	    elif letter == '-':
		stack.append(op2 - op1)
	    elif letter == '*':
		stack.append(op2 * op1)
	    else:
		stack.append(op2 / op1)
	else:
	    stack.append(float(letter))
    
    if len(stack) > 0:
	res = stack.pop()
	if res.is_integer(): return int(res)
	return res
    else:
	return 0

test.assert_equals(calc(""), 0)
test.assert_equals(calc("1 2 3"), 3)
test.assert_equals(calc("1 2 3.5"), 3.5)
test.assert_equals(calc("1 3 +"), 4)
test.assert_equals(calc("1 3 *"), 3)
test.assert_equals(calc("1 3 -"), -2)
test.assert_equals(calc("4 2 /"), 2)
