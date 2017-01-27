from operator import itemgetter

def _find_stats(word):
    num_letters = 0
    num_digits = 0

    for letter in word:
	if letter.isalpha():
	    num_letters = num_letters + 1
	elif letter.isdigit():
	    num_digits = num_digits + 1
	else:
	    # this is not eligible word
	    return (False, num_letters, num_digits)

    if (num_letters % 2 == 0) and (num_digits % 2 == 1):
	return(True, num_letters, num_digits)
    else:
	return (False, num_letters, num_digits)

def solution(S):
    words = [s.strip() for s in S.split(' ')]
    eligible_words = []

    for word in words:
	(eligible, num_letters, num_digits) = _find_stats(word = word)
	if eligible:
	    eligible_words.append({
		'word' : word,
		'num_letters' : num_letters,
		'num_digits' : num_digits,
		'len' : num_letters + num_digits
	    })
    words = sorted(eligible_words, key = itemgetter('len'), reverse = True)
    if words:
	return words[0]['len']
    else:
	return -1

if __name__ == '__main__':
    # one character words only
    print solution(S = 'A')
    print solution(S = 'A b 4 ? g 9')
    print solution(S = 'test 5 a0A pass007 ?xy1')