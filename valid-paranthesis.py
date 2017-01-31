import test

def valid_parantheses(string):
    stack = []

    for letter in string:
	if letter not in ['(', ')']: continue
	if len(stack) == 0: stack.append(letter)
	else:
	    if letter == ')' and stack[len(stack) - 1] == '(':
		stack.pop()
	    else:
		stack.append(letter)
    
    return len(stack) == 0

test.assert_equals(valid_parantheses('()'), True)
test.assert_equals(valid_parantheses(')(()))'), False)
test.assert_equals(valid_parantheses('('), False)
test.assert_equals(valid_parantheses('(())((()())())'), True)