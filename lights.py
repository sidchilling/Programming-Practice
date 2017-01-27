
def _get_freq_map(segment):
    d = {}
    for letter in segment:
	if d.get(letter, None):
	    d[letter] = d[letter] + 1
	else:
	    d[letter] = 1
    return d

def _check_for_even_segment(freq_map):
    num = freq_map[freq_map.keys()[0]] # get the first frequency
    for key, freq in freq_map.iteritems():
	if freq % 2 != 0 or freq != num:
	    return False # this is not a valid segment
    return True # a valid segment

def _check_for_odd_segment(freq_map):
    even_freq = 0
    odd_freq = 0

    for key, freq in freq_map.iteritems():
	if freq % 2 == 0:
	    # this is even
	    if even_freq == 0: even_freq = freq
	    elif freq != even_freq: return False
	    else:
		continue # this frequency is ok
	else:
	    # this is odd
	    if odd_freq == 0: odd_freq = freq
	    else: 
		# there cannot be two odd frequencies
		return False
    if odd_freq == 1: return True
    elif odd_freq == (even_freq + 1): return True
    else:
	return False

def _is_segment_valid(segment):
    freq_map = _get_freq_map(segment)
    if len(segment) % 2 == 0:
	# even - all the frequencies must be the same and even
	return _check_for_even_segment(freq_map = freq_map)
    else:
	# odd - all, except one, frequences must be the same and even
	# the one that is not the same must be odd and one more than the above
	return _check_for_odd_segment(freq_map = freq_map)

def solution(S):
    res = 0 # the number of possibilities
    
    for num_lights in range(1, len(S) + 1):
	for start_index in range(0, len(S) - num_lights + 1):
	    segment = S[start_index : start_index + num_lights]
	    if _is_segment_valid(segment = segment):
		res = res + 1
	
    return res

if __name__ == '__main__':
    print solution(S = '02002')