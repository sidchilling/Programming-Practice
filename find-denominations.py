

def _get_max(change, d):
    num = 0
    while change > 0:
	if (num + 1) * d > change:
	    break
	else:
	    num = num + 1
	    change = change - (num * d)
    return num

def getChange(M, P):
    change = M - P # return this much

    denominations = [1, 0.5, 0.25, 0.1, 0.05, 0.01] 
    res = []
    d_index = 0

    # we start with the highest denonimation
    for d in denominations:
	num_d = _get_max(change, d)
	change = change - (num_d * d)
	res.append(num_d)
	if change > 0:
	    continue
	else:
	    break

    # res should contain the result
    if len(res) < len(denominations):
	res_len = len(res)
	for i in range(0, len(denominations) - res_len):
	    res.append(0)
    
    return res

print getChange(M = 10, P = 1.2)
	