
def find_num_matching(s):
    
    s = s.strip()
    chains = s.split(',')
    chains = [x.split('-') for x in chains]
    
    max_num = 0
    current_num = 0

    for index in range(1, len(chains)):
	prev = chains[index - 1]
	current = chains[index]
	
	if int(prev[1].strip()) == int(current[0].strip()):
	    current_num = current_num + 1
	else:
	    current_num = 0
	
	max_num = max(max_num, current_num)

    max_num = max_num + 1
    return max_num

'''
print find_num_matching('1-4, 4-2, 3-1')
print find_num_matching('6-3')
print find_num_matching('4-3,5-1,2-2,1-3,4-4')
print find_num_matching('2-4,4-1')
print find_num_matching('5-2,1-6')
print find_num_matching('1-1,3-5,5-2,2-3,2-4')
print find_num_matching('1-1,3-5,5-2,2-3,2-4,3-5,5-3,3-3,3-4')
'''

print find_num_matching('1-1')
print find_num_matching('1-2,1-2')
print find_num_matching('3-2,2-1,1-4,4-4,5-4,4-2,2-1')
print find_num_matching('5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5')
print find_num_matching('1-1,3-5,5-5,5-4,4-2,1-3')
print find_num_matching('1-2,2-2,3-3,3-4,4-5,1-1,1-2')