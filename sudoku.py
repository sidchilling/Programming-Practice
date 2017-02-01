import test

def _init_tracker():
    return [False] * 9

def _check_rows(board):
    for row in board:
	tracker = _init_tracker()
	for num in row:
	    if not tracker[num - 1]: tracker[num - 1] = True
	    else:
		# repitition
		return False
	for el in tracker:
	    if not el: return False
    return True

def _check_cols(board):
    for col_num in range(0, 9):
	tracker = _init_tracker()
	for row_num in range(0, 9):
	    if not tracker[board[row_num][col_num] - 1]:
		tracker[board[row_num][col_num] - 1] = True
	    else:
		return False
	for el in tracker:
	    if not el: return False
    return True

def _check_regions(board):
    ranges = [range(0, 3), range(3, 6), range(6, 9)]

    for row_range in ranges:
	for col_range in ranges:
	    tracker = _init_tracker()
	    for row_num in row_range:
		for col_num in col_range:
		    if not tracker[board[row_num][col_num] - 1]:
			tracker[board[row_num][col_num] - 1] = True
		    else:
			return False
	    for el in tracker:
		if not el: return False
    return True
	    

def done_or_not(board):

    # board is a list of list

    # check for all rows first
    if not _check_rows(board) or not _check_cols(board) or not _check_regions(board):
	return 'Try again!'
    else:
	return 'Finished!'

board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
	 [6, 7, 2, 1, 9, 5, 3, 4, 8],
	 [1, 9, 8, 3, 4, 2, 5, 6, 7],
	 [8, 5, 9, 7, 6, 1, 4, 2, 3],
	 [4, 2, 6, 8, 5, 3, 7, 9, 1],
	 [7, 1, 3, 9, 2, 4, 8, 5, 6],
	 [9, 6, 1, 5, 3, 7, 2, 8, 4],
	 [2, 8, 7, 4, 1, 9, 6, 3, 5],
	 [3, 4, 5, 2, 8, 6, 1, 7, 9]]
test.assert_equals(done_or_not(board), 'Finished!')

board = [[1, 3, 2, 5, 7, 9, 4, 6, 8], 
	[4, 9, 8, 2, 6, 1, 3, 7, 5],
	[7, 5, 6, 3, 8, 4, 2, 1, 9],
	[6, 4, 3, 1, 5, 8, 7, 9, 2],
	[5, 2, 1, 7, 9, 3, 8, 4, 6],
	[9, 8, 7, 4, 2, 6, 5, 3, 1],
	[2, 1, 4, 9, 3, 5, 6, 8, 7],
	[3, 6, 5, 8, 1, 7, 9, 2, 4],
	[8, 7, 9, 6, 4, 2, 1, 5, 3]]
test.assert_equals(done_or_not(board), 'Finished!')

board = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
	[4, 9, 8, 2, 6, 1, 3, 7, 5],
	[7, 5, 6, 3, 8, 4, 2, 1, 9],
	[6, 4, 3, 1, 5, 8, 7, 9, 2],
	[5, 2, 1, 7, 9, 3, 8, 4, 6],
	[9, 8, 7, 4, 2, 6, 5, 3, 1],
	[2, 1, 4, 9, 3, 5, 6, 8, 7],
	[3, 6, 5, 8, 1, 7, 9, 2, 4],
	[8, 7, 9, 6, 4, 2, 1, 3, 5]]
test.assert_equals(done_or_not(board), 'Try again!')