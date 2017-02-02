
def cmp_func(item1, item2):
    if item1['frequency'] < item2['frequency']:
	return -1
    elif item1['frequency'] > item2['frequency']:
	return 1
    else:
	# frequencies are equal
	if item1['quantity'] < item2['quantity']:
	    return -1
	else:
	    return 1

def get_rock_index(quantity):
    jamie = quantity
    ned = sorted(quantity)

    freq = {}
    for index in range(0, len(jamie)):
	target_q = jamie[index] + ned[index]
	if freq.get('{}'.format(target_q), None):
	    freq['{}'.format(target_q)]['freq'] += 1
	    freq['{}'.format(target_q)]['highest_index'] = index
	else:
	    freq['{}'.format(target_q)] = {
		'freq' : 1,
		'highest_index' : index
	    }
    
    # now find the highest among freq
    freq_l = []
    for quantity, m in freq.iteritems():
	freq_l.append({
	    'quantity' : int(quantity),
	    'frequency' : int(m['freq']),
	    'highest_index' : int(m['highest_index'])
	})

    freq_l = sorted(freq_l, cmp = cmp_func, reverse = True)
    return freq_l[0]['highest_index']

print get_rock_index(quantity = [5, 5, 9, 19, 2, 2])
print get_rock_index(quantity = [10, 10, 7, 7, 7, 2, 7, 2])