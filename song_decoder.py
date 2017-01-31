import test

def _strip(song, dubstep):
    while song.startswith(dubstep):
	song = song[len(dubstep) :]
    while song.endswith(dubstep):
	song = song[0 : len(song) - len(dubstep)]
    return song

def song_decoder(song):
    dubstep = 'WUB'
    song = _strip(song = song, dubstep = dubstep)
    
    while song.find(dubstep) != -1:
	# replace each WUB with space
	start_index = song.find(dubstep)
	end_index = start_index + len(dubstep)

	if song[start_index - 1] != ' ':
	    # we have to insert a space
	    song = '{} {}'.format(song[0 : start_index], song[end_index :])
	else:
	    # dont insert a space
	    song = '{}{}'.format(song[0 : start_index], song[end_index :])
    
    return song

test.assert_equals(song_decoder('AWUBBWUBC'), 'A B C')
test.assert_equals(song_decoder('AWUBWUBWUBBWUBWUBWUBC'), 'A B C')
test.assert_equals(song_decoder('WUBAWUBBWUBCWUB'), 'A B C')
test.assert_equals(song_decoder('IWUBAMWUBJBWUB'), 'I AM JB')