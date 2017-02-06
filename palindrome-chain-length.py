import test

def _is_palindrome(n):
    n = '{}'.format(n)
    return True if n == n[::-1] else False

def _operate(n):
    n = '{}'.format(n)
    return int(n) + int(n[::-1])

def palindrome_chain_length(n):
   num_steps = 0

   while not _is_palindrome(n):
       n = _operate(n)
       num_steps = num_steps + 1
   return num_steps

test.assert_equals(palindrome_chain_length(5), 0)
test.assert_equals(palindrome_chain_length(87), 4)