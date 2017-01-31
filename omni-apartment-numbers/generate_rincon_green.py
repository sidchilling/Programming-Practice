
def _two_digit(number):
    number = '{}'.format(number)
    if len(number) >= 2: return number
    else:
	return '0{}'.format(number)




