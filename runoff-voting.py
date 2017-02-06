import test

from operator import itemgetter

def _get_ordered_votes(voters):
    d = {}
    for voter in voters:
	if d.get(voter[0], None):
	    d[voter[0]] += 1
	else:
	    d[voter[0]] = 1
    # convert to list
    dl = []
    for candidate, num in d.iteritems():
	dl.append({
	    'num' : num,
	    'candidate' : candidate
	})
    return sorted(dl, key = itemgetter('num'), reverse = True)

def get_removal_candidates(vl):
    res = []
    min_num = vl[len(vl) - 1]['num']

    for index in range(len(vl) - 1, -1, -1):
	if vl[index]['num'] == min_num:
	    res.append(vl[index]['candidate'])
    
    return res

def remove_least(v, r):
    for cd in r:
	try:
	    v.remove(cd)
	except:
	    continue
    return v

def has_remaining_votes(voters):
    for v in voters:
	if len(v) > 0: return True
    return False

def runoff(voters):

    while True:
	if has_remaining_votes(voters):
	    votes_orders = _get_ordered_votes(voters)
	    if votes_orders[0]['num'] > len(voters) / 2:
		return votes_orders[0]['candidate']

	    # we will have to remove the least ones
	    remove_candidates = get_removal_candidates(vl = votes_orders)
	    new_voters = []
	    for v in voters:
		new_voters.append(remove_least(v, remove_candidates))
	    voters = new_voters
	else:
	    return None

voters = [['dem', 'ind', 'rep'],
	  ['rep', 'ind', 'dem'],
	  ['ind', 'dem', 'rep'],
	  ['ind', 'rep', 'dem']]
test.assert_equals(runoff(voters), 'ind')

voters = [['a', 'c', 'd', 'e', 'b'],
	  ['e', 'b', 'd', 'c', 'a'],
	  ['d', 'e', 'c', 'a', 'b'],
	  ['c', 'e', 'd', 'b', 'a'],
	  ['b', 'e', 'a', 'c', 'd']]
test.assert_equals(runoff(voters), None)