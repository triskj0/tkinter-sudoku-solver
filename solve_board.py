# returns row, col
def find_empty_spot(board):
	for r in range(9):
		for c in range(9):
			if board[r][c] == 0:
				return r, c
	return None, None


# returns bool
def is_valid(board, guess, row, col):
	row_vals = board[row]
	# check rows
	if guess in row_vals:
		return False

	# check colums
	for r in range(9):
		if board[r][col] == guess:
			return False

	# check 3x3 square
	col_start = (col // 3) * 3
	row_start = (row // 3) * 3

	for r in range(row_start, row_start + 3):
		for c in range(col_start, col_start + 3):
			if board[r][c] == guess:
				return False

	return True


def solve(board):
	row, col = find_empty_spot(board)
	if row == None:
		return True

	for guess in range(1, 10):
		if is_valid(board, guess, row, col):
			board[row][col] = guess
			
			if solve(board):
				return True

		board[row][col] = 0
	return False
