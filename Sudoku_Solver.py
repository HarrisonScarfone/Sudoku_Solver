#brute force sudoku solver
#by: Harrison Scarfone

class Sudoku:

	def __init__(self, filepath):
		file = open(filepath)
		line = file.readline()
		self.puzzle = {}
		choices = [1,2,3,4,5,6,7,8,9]
		cell = 0
		while line:
			cell_input = line.split(',')
			for num in cell_input:
				try:
					if int(num) and int(num) in choices:
						choices.remove(int(num))
						self.puzzle[cell] = int(num)
				except:
					self.puzzle[cell] = choices
				cell += 1
			choices = [1,2,3,4,5,6,7,8,9]
			line = file.readline()

	def display_cell_key(self):
		count = 0
		display_string = ''
		for key in self.puzzle:
			if count % 9 == 0:
				count = 0
				print(display_string)
				display_string = ''
			display_string += str(key) + '\t'
			count += 1

	def display_possible_cell_values(self):
		display_string = ''
		for cell in self.puzzle:
			print('cell: ' + str(cell) + ' ' +  str(self.puzzle[cell]) + '  ' )

	def tester(self):
		for i in range(9):
			removals = []
			for j in range(9):
				if type(self.puzzle[i + 9 * j]) is int:
					removals.append(self.puzzle[i + 9 * j])
			for number in removals:
				for k in range(9):
					if type(self.puzzle[i + 9 * k]) is int:
						print('found an int')
						continue
					else:
						try:
							new_list = self.puzzle[i + 9 * k]
							print(new_list)
							new_list.remove(number)
							print(new_list)
							if len(new_list) == 1:
								self.puzzle[i + 9 * k] = new_list[0]
							else:
								self.puzzle[i + 9 * k] = new_list
						except:
							print('error, skipping')
							pass
			# 	print(str(cell) + ' trying to remove ' + str(removing_number))
			# 	for i in range (9):
			# 		if type(self.puzzle[column_number + 9 * i]) is int:
			# 			print(str(cell) + 'skipping this number because it returned type int')
			# 			continue
			# 		else:
			# 			try:
			# 				possible_nums = self.puzzle[column_number + (9 * i)]
			# 				print(str(possible_nums) + 'this is what possible are')
			# 				if removing_number in possible_nums:
			# 					possible_nums.remove(removing_number)
			# 					print(str(possible_nums) + ' this is with number removed')
			# 				if len(possible_nums) == 1:
			# 					to_int = int(possible_nums[0,1])
			# 					self.puzzle[column_number + 9 * i] = to_int
			# 					print(str(self.puzzle[column_number + 9 * i]) + 'this changed list to int')
			# 					continue
			# 				self.puzzle[column_number + 9 * i] = possible_nums
			# 				print(str(self.puzzle[column_number + 9 * i]) + ' inserted original list')
			# 				#print('{}: {}'.format(column_number + 9 * i, self.puzzle[cell]))
			# 			except:
			# 				continue
			# print('onto the next cell')

	def check_boxes(self):
		box1 = [0,1,2,9,10,11,18,19,20]
		box2 = [3,4,5,12,13,14,21,22,23]
		box3 = [6,7,8,15,16,17,24,25,26]
		box4 = [27,28,29,36,37,38,45,46,47]
		box5 = [30,31,32,39,40,41,48,49,50]
		box6 = [33,34,35,42,43,44,51,52,53]
		box7 = [54,55,56,63,64,65,72,73,74]
		box8 = [57,58,59,66,67,68,75,76,77]
		box9 = [60,61,62,69,70,71,78,79,80]
		boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

		for box in boxes:
			for cell in box:
				if type(self.puzzle[cell]) is int:
					for nums in box:
						if type(self.puzzle[nums]) is int:
							continue
						else:
							possible_nums = self.puzzle[nums]
							if len(possible_nums) == 1:
								to_int = possible_nums[0]
								self.puzzle[nums] = to_int
							else:
								self.puzzle[nums] = possible_nums




test = Sudoku('sudoku.txt')
# test.display_cell_key()
# test.display_possible_cell_values()
#test.display_possible_cell_values()
test.tester()
#test.display_possible_cell_values()
# test.check_boxes()
print(test.puzzle)


