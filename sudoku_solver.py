from tkinter import *
import tkinter.font as font
from PIL import Image

from check_board_validity import *
from solve_board import *

root = Tk()
root.title('Sudoku Solver')

# background
bg = PhotoImage(file='blank-sudoku.png')
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)

# window geometry
w, h = Image.open('blank-sudoku.png').size
root.geometry(f'{w}x{h+80}')

# font
my_font = font.Font(family='Helvetica', size=27, weight='bold')

# validation for entries
def validate(e):
	if len(e) == 0 or len(e) == 1 and e.isdigit():
		return True
	return False


valcmd = (root.register(validate), '%P')

# text fields
entries = []
for row in range(9):
	for col in range(9):
		e = Entry(root, validate='key', validatecommand=valcmd, width=2,\
				 justify='center', font=my_font, borderwidth=2)
		e.grid(row=row, column=col, columnspan=1, padx=9.5, pady=8)
		entries.append(e)


def show_invalid_label():
	invalid_input_label = Label(root, text='Invalid Input', height=16, width=27, font=my_font, bg='white')
	invalid_input_label.grid(row=0, column=0, columnspan=1)
	root.after(2000, lambda: invalid_input_label.destroy())


# functions for buttons
def solve_command():
	new_board = [[] for i in range(9)]

	# get input
	for e in enumerate(entries):
		val = e[1].get()
		board_index = e[0]//9
		if val == '':
			new_board[board_index].append(0)
			continue
		new_board[board_index].append(int(val))
	
	# check for input validity
	if validate_board(new_board) == False:
		show_invalid_label()
		return

	# don't do anything if there's no input
	if all([e.get() == '' for e in entries]):
		return

	solve(new_board)

	# any 0s in new_board => invalid input
	if any([0 in r for r in new_board]):
		show_invalid_label()
	else:
		for r in range(9):
			for c in range(9):
				index = 9*r+c
				if str(new_board[r][c]) != entries[index].get():
					entries[index].insert(0, str(new_board[r][c]))


def clear_command():
	for e in entries:
		e.delete(0, END)

# buttons
solve_button = Button(root, text='Solve', padx=135, font=my_font, command=solve_command)
clear_button = Button(root, text='Clear', padx=35, font=my_font, command=clear_command)

solve_button.grid(row=82, column=0, columnspan=6)
clear_button.grid(row=82, column=6, columnspan=3)


root.mainloop()