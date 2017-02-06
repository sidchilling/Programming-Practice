
def capitalize(s):
    punctuations = ['.', '?', '!', ',', ':', ';']

    res = ''
    make_cap = True
    punc = False
    index = 0

    for letter in s:
	
	if index > 0:
	    if res[len(res) - 1] == ' ' and letter == ' ':
		continue

	if letter in punctuations:
	    punc = True
	if punc:
	    # check if the previous is a space
	    if res[len(res) - 1] == ' ':
		res = res[0 : len(res) - 1]
	    res = '{}{} '.format(res, letter)
	    punc = False
	    if letter in ['.', '?', '!']:
		make_cap = True
	elif make_cap:
	    res = '{}{}'.format(res, letter.upper())
	    make_cap = False
	else:
	    res = '{}{}'.format(res, letter)
	
	index = index + 1
    
    if res[len(res) - 1] == ' ':
	res = res[0 : len(res) - 1]
    return res

print capitalize(s = 'first, solve the problem.then,write the code.')
print capitalize(s = 'this is a test... and another test.')
print capitalize('Hi!')
print capitalize('hi, this is me.everyone listening?good!')
print capitalize('hello. how are you today? great! i\'m fine too')
print capitalize('do.or do not. there is no try.')
print capitalize('the house is on fire!?run!')
print capitalize('the conference has people who have come from Moscow,Idaho;Paris,Texas;London,Ohio; and other places as well.')
