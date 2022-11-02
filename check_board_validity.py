def validate_board(board):
	# check rows
	for r in range(9):
		row_vals = board[r]		
		row_vals = list(filter(lambda x: x != 0, row_vals))

		if len(set(row_vals)) != len(row_vals):
			return False	

	# check columns
	for c in range(9):
		col_vals = [board[r][c] for r in range(9)]
		col_vals = list(filter(lambda x: x != 0, col_vals))

		if len(set(col_vals)) != len(col_vals):
			return False

	# check squares
	for s in range(9):
		square_vals = []
		row_start = s // 3 * 3
		col_start = s // 3 * 3

		for r in range(row_start, row_start+3):
			for c in range(col_start, col_start+3):
				square_vals.append(board[r][c])

		square_vals = list(filter(lambda x: x != 0, square_vals))

		if len(set(square_vals)) != len(square_vals):
			return False

	return True