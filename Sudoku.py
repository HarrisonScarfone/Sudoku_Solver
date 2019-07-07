#===========================================================================================================================================
#brute force sudoku solver
#by: Harrison Scarfone
#===========================================================================================================================================
# Algorithm:
# 1.Find the next cell that needs a value
# 2.If the cell you need a value from is signifying the end of the puzzle, return True and the puzzle is solved
# 3.If it's not the end of the puzzle, then try numbers 1 to 9
# 4.When a valid number is found for the cell that needs a value, mark that value, update the sudoku matrix and recursively call solve
# 5.If solve returns True weve solved the puzzle so return True and break solve method
# 6.If solve doesnt return true, reset the index that was modified and iterate up in possible numbers
# 7.If we cant find a solution, return False
# 8. Runtime -> O(a very big number)
#===========================================================================================================================================
#create a class to contain the sudoku
class Sudoku:
	#sudoku intializes by reading in a csv file, each row must be seperated
	def __init__(self, filepath):
		file = open(filepath)
		line = file.readline()
		self.row = 0
		self.col = 0
		self.puzzle = []
		while line:
			append_this = []
			col_idx = 0
			this_lines_numbers = line.split(',')
			for number in this_lines_numbers:
				try:
					int(number)
					append_this.append(int(number.strip()))
				except:
					append_this.append(0)
			self.puzzle.append(append_this)
			line = file.readline()
	#method to print the current state of the puzzle		
	def print_current(self):
		for i in range(9):
			print_string = ''
			for j in range(9):
				print_string += '{}\t'.format(self.puzzle[i][j])
			print(print_string)
	#check a cells value against the values already existing in the row
	def check_row(self, puzzle, row, number):
		for row_check in range(9):
			if puzzle[row][row_check] == number:
				return False
		return True
	#check a cells value against the values already existing in a column
	def check_col(self, puzzle, col, number):
		for column_check in range(9):
			if puzzle[column_check][col] == number:
				return False
		return True
	#check a cells value against the values already existing in a box
	def check_box(self, puzzle, row, col, number):
		start_row = row - row % 3
		start_col = col - col % 3
		for c1 in range(3):
			for c2 in range(3):
				if puzzle[start_row + c1][start_col + c2] == number:
					return False
		return True
	#method to call row, col, box checks and return true if a current value could possibly yeild a solution
	def check_element(self, puzzle, row, col, number):
		if self.check_row(puzzle, row, number) and self.check_col(puzzle, col, number) and self.check_box(puzzle, row, col, number):
			return True
		return False
	#when solve recurses, this method will move the current cell to the next cell that needs fillings
	def next_zero_cell(self):
		for i in range(9):
			for j in range(9):
				if self.puzzle[i][j] == 0:
					return i,j
		return -1,-1
	#main method that will solve the puzzle - see algorithm notes at top
	def solve(self):
		zero_cell = self.next_zero_cell()
		zero_row = zero_cell[0]
		zero_col = zero_cell[1]
		if zero_cell[0] == -1:
			return True
		for trying_num in range(1, 10):
			if self.check_element(self.puzzle, zero_row, zero_col, trying_num):
				self.puzzle[zero_row][zero_col] = trying_num
				if self.solve():
					return True
				self.puzzle[zero_row][zero_col] = 0
		return False
#driver
test = Sudoku('sudoku.txt')
test.solve()
test.print_current()



