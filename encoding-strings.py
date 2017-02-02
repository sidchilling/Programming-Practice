
def is_vowel(letter):
    return True if letter in ['a', 'e', 'i', 'o', 'u'] else False

def get_num(letter):
    return ord(letter) - ord('a') + 1

def get_char(letter_sum):
    return chr(letter_sum + ord('a') - 1)

def get_encoded_letter(current_letter, next_letter):
    letter_sum = get_num(current_letter) + get_num(next_letter)
    if letter_sum > 26:
	letter_sum = letter_sum % 26
    return get_char(letter_sum)

def encode_string(s):
    s = s.lower()
    res = ''
    occurred = {}
    
    m = ''
    for letter in s:
	if is_vowel(letter): continue
	if occurred.get(letter, None): continue
	else:
	    # this has to be considered
	    m = '{}{}'.format(m, letter)
	    occurred[letter] = 1

    # now we will use the encryption algorithm
    for index in range(0, len(m)):
	current_letter = m[index]
	next_letter = m[0] if index == (len(m) - 1) else m[index + 1]
	res = '{}{}'.format(res, get_encoded_letter(current_letter = current_letter,
					    next_letter = next_letter))

    return res

print encode_string(s = 'bcd')
print encode_string(s = '{}y{}'.format('yx' * 17, 'io' * 5))
print encode_string(s = '')
print encode_string(s = 'b')