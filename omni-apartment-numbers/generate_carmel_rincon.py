
def _two_digit(num):
    num = '{}'.format(num)
    if len(num) == 2:
	return num
    else:
	return '0{}'.format(num)

## Carmel Ricon
# ---------------
# 320 units
# 22 Stories

# Possible apartment numbers - 
# 906, 1906, 1613, 2117, 1219, 1711, 2117, 1712, 1214, 1109, 1717, 1020, 1816
# 1814, 2003, 905

## Rincon Green
# ------------
# 326 Units
# 7 Stories
## Possible apartment numbers from our list -
# 3, 105, 239, 246, 341, 314, 369, 439, 461, 405, 564, 537, 614

# Looks like the story number starts from zero through 6 (as there is a 
# apartment number 3 in our records)

# However, it seems like 369 is also there, which we will not be able to generate

## Lumnia
# -------
# 650 Units, 42 Stories
# Possible Apartment numbers from our records - 
# 30D, 14B, 16F, 20A
# 4 Towers
# Plaza A - 8 stories
# Tower B - 42 stories
# Plaza C - 8 Stories
# Tower D - 37 Stories
# Can't see a pattern in Lumina

## Millenium Tower
# ----------
# 419 Units, 58 Stories
# Possible Apartment numbers from our records - 
# 12D, 49D, 48A, 27F, 48A, 22A, 603
# Can't find anything here

## Infinity Towers
# ------------
# 650 Units
# 2 Low Rise Buildings - 8 stories and 9 stories
# 2 High Rise Buildings - 37 and 42 stories
# 35A, 31F, 19H, 7D 
# Can't find any pattern or other information

## One Rincon Hill
# ---------------
# North Tower - 50 stories, South Tower - 60 stories
# 709 Units
# Apartment numbers from our records - 
# 4005, 3402, 1008, 3102, 3106, 3702, 4408
# Doesn't add up

def _add_apartment(apartments_list):
    res = '{}'.format(int(apartments_list[len(apartments_list) - 1]) + 1)
    return res

def _total_num_apartments(all_apartments):
    res = 0
    for floor in all_apartments:
	res = res + len(floor)
    return res

apartment_numbers = []
num_stories = 7
num_units = 326

num_apartments = 0

for num_story in range(0, num_stories):
    current_story_flats = []
    for num_apartment in range(1, (num_units / num_stories) + 1):
	if num_story > 0:
	    current_story_flats.append('{}{}'.format(num_story, _two_digit(num_apartment)))
	else:
	    current_story_flats.append('{}'.format(num_apartment))
	num_apartments = num_apartments + 1
    apartment_numbers.append(current_story_flats)

units_left = num_units - num_apartments

apartment_numbers_index = 0
while units_left > 0:
    apartment_numbers[apartment_numbers_index].append(_add_apartment(apartment_numbers[apartment_numbers_index]))
    apartment_numbers_index += 1
    if apartment_numbers_index >= len(apartment_numbers):
	apartment_numbers_index -= 1
    units_left = units_left - 1

for floor in apartment_numbers:
    for apt_num in floor:
	print '{}'.format(apt_num)

print 'Total number of apartments: {}'.format(_total_num_apartments(apartment_numbers))