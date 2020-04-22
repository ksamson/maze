# A recursive backtracker implementation of the maze-generation algorithm

from grid import Grid
from PIL import Image, ImageDraw

def main():
	# Creates a grid object with row x col cell objects
	g = Grid(3,3, cell_size=50)
	g.draw_grid()
	_test(g.grid)

	# Pseudocode : https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
	# stack = []
	# initial_cell = g[0] 
	# stack.append(initial_cell)

	# while len(stack) != 0:
	# 	current_cell = stack.pop()
	# 	# Step 1: Push the current cell to the stack (if there are unvisited neighbors)
	# 	if current_cell.check_neighbors() == True:
	# 		stack.append(current_cell)

	# 		# Step 2: Choose one of the unvisited neighbors
	#		# TODO: Implement below function
	# 		unvisited_neighbor_cell = current_cell.get_unvisited_neighbor()
			
	#  		# Step 3: Remove the wall between the current and chosen cell
	#		# TODO: Implement below function
	#  		# current_cell.remove_wall(unvisited_neighbor_cell)
			
	# 		# Step 4: Mark the chosen cell as visited and push it into the stack
	# 		un.visited = True
	# 		stack.append(un)

# TODO: create a unit test
def _test(grid):
	first_cell = grid[0]
	second_cell = grid[1]
	for i in range(len(grid)):
		print(i, grid[i])

	print("========================")
	print(first_cell)
	print(second_cell)
	print("========================")
	print("first cell's right neighbor should be (0,1):", first_cell.right)
	print("second cell's right neighbor should be (0,2): ",second_cell.right)
	print("========================")
	print("first cell's right neighbor should be equal to second_cell:", first_cell.right == second_cell)
	print("second cell's left neighbor should be equal to first_cell:", first_cell.right == second_cell)

if __name__ == "__main__":
	main()
