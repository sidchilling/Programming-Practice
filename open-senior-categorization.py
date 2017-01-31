import test

def openOrSenior(data):
    res = []
    
    for person in data:
	if person[0] >= 55 and person[1] > 7:
	    res.append('Senior')
	else:
	    res.append('Open')
    
    return res

test.assert_equals(openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]),
			       ['Open', 'Senior', 'Open', 'Senior'])
test.assert_equals(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]),
				['Open', 'Open', 'Senior', 'Open'])