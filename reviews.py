import sys
import string
from operator import itemgetter


valid = string.lowercase + string.digits + string.whitespace
table = string.maketrans(valid, valid)
remove = ''.join(set(string.printable) - set(valid))

def count_occurence(word, review):
    return review.lower().translate(table, remove).split().count(word)

def count_occurences(words, reviews):
    return [sum(c in words for c in word) for review.lower().translate(table, remove).split() in reviews]

if __name__ == '__main__':
    stop_words = raw_input()
    stop_words = stop_words.split(' ') # these are the words we have to find

    hotels = {}

    num_reviews = int(raw_input())

    for i in range(0, num_reviews):
	hotel_id = raw_input()
	if not hotels.get(hotel_id, None):
	    #if hotel_id not in hotels.keys():
	    hotels[hotel_id] = {
		'reviews' : []
		'num_occurences' : 0
	    }
	review = raw_input()
	hotels[hotel_id]['reviews'].append(review)
	for word in stop_words:
	    hotels[hotel_id]['num_occurences'] += count_occurence(word, review)
    
    hotels_list = []

    for hotel_id in hotels.keys():
	hotels_list.append({'hotel_id' : int(hotel_id), 'num_occurences' : hotels[hotel_id]['num_occurences']})

    hotels_list = sorted(hotels_list, key = itemgetter('hotel_id'), reverse = True)
    hotels_list = sorted(hotels_list, key = itemgetter('num_occurences'), reverse = True)

    res = ''
    for hotel in hotels_list:
	res = '{} {}'.format(res, hotel['hotel_id'])
    res = res.strip()
    print '{}'.format(res)
    