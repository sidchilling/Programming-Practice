import test

def _get_freq(s):
    d = {}
    for letter in s:
	if letter.islower():
	    if d.get(letter, None):
		d[letter] = d[letter] + 1
	    else:
		d[letter] = 1
    return d

def cmp_func(item1, item2):
    if len(item1['letters']) < len(item2['letters']):
	return -1
    elif len(item1['letters']) > len(item2['letters']):
	return 1
    else:
	# equal
	if item1['letters'][0] < item2['letters'][1]:
	    return 1
	else:
	    return -1

def mix(s1, s2):
    s1_freq = _get_freq(s1)
    s2_freq = _get_freq(s2)
    
    res = []
    for letter in s1_freq.keys():
	if s2_freq.get(letter, None):
	    # this letter is present in s2
	    if max(s1_freq[letter], s2_freq[letter]) > 1:
		# this has to be considered
		string_num = '='
		if s1_freq[letter] > s2_freq[letter]:
		    string_num = '1'
		elif s2_freq[letter] > s1_freq[letter]:
		    string_num = '2'
		res.append({
		    'string_num' : '{}'.format(string_num),
		    'letters' : '{}'.format(letter) * max(s1_freq[letter], 
					   s2_freq[letter])
		})
		del s2_freq[letter]
	else:
	    # this letter is not present in s2
	    if s1_freq[letter] > 1:
		res.append({
		    'string_num' : '1',
		    'letters' : '{}'.format(letter) * s1_freq[letter]
		})

    # remaining letters in s2
    for letter in s2_freq.keys():
	if s2_freq[letter] > 1:
	    res.append({
		'string_num' : '2',
		'letters' : '{}'.format(letter) * s2_freq[letter]
	    })

    # sort res
    res = sorted(res, cmp = cmp_func, reverse = True)

    res_str = ''
    for d in res:
	res_str = '{}{}:{}/'.format(res_str, d['string_num'], d['letters'])
    res_str = res_str[0 : len(res_str) - 1]
    return res_str

print mix(s1 = 'my&friend&Paul has heavy hats! &',
	 s2 = 'my friend John has many many friends &')