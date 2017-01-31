import test

MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
	      '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
	      '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
	      '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
	      '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6',
	      '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.',
	      '--': 'M', '-.': 'N', '....': 'H', '.----.': "'",
	      '...-': 'V', '--...': '7', '-.-.-.': ';', '-....-': '-',
	      '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
	      '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+',
	      '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T',
	      '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
	      '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8',
	      '...--': '3'}


def decodeMorse(morseCode):
    morseCode = morseCode.strip() # remove extra spaces from the start and end
    # letters are separated by one space
    # words are separated by three spaces
    words = morseCode.split('   ') # split by 3 spaces
    morseCode = [word.split(' ') for word in words]

    decoded = ''
    
    for word in morseCode:
	for letter in word:
	    decoded = '{}{}'.format(decoded, MORSE_CODE[letter])
	decoded = '{} '.format(decoded)

    return decoded.strip() # remove the last extra space

test.assert_equals(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')