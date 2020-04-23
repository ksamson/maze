# A recursive backtracker implementation of the maze-generation algorithm

from grid import Grid
from PIL import Image, ImageDraw
import random
import imageio
import os

def main():
	# Creates a grid object with row x col cell objects
	g = Grid(10,10, cell_size=50)
	frame = 0
	filenames = []
	#_test(g.grid)

	# Pseudocode : https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker
	stack = []
	initial_cell = g.grid[0]
	initial_cell.visited = True
	stack.append(initial_cell)

	while len(stack) != 0:
		current_cell = stack.pop()
		neighbors = current_cell.get_unvisited_neighbor()

		# Step 1: Push the current cell to the stack (if there are unvisited neighbors)
		if neighbors:
			stack.append(current_cell)


			# Step 2: Choose one of the unvisited neighbors
			unvisited_neighbor_cell = random.choice(neighbors)
			unvisited_neighbor_cell.current = True
	 		# Step 3: Remove the wall between the current and chosen cell
			current_cell.remove_wall(unvisited_neighbor_cell)
			
			# Step 4: Mark the chosen cell as visited and push it into the stack
			unvisited_neighbor_cell.visited = True
			stack.append(unvisited_neighbor_cell)

			# Below are for gif creation
			frame += 1
			g.draw_grid(str(frame))
			filenames.append("./exports/maze"+str(frame)+".png")
			unvisited_neighbor_cell.current = False

	create_gif(filenames, 'recursive_backtracker.gif', 5)
	g.draw_grid()

def create_gif(filenames, moviename, fps=10):
    frames = []
    # Create gif
    for filename in filenames:
        frames.append(imageio.imread(filename))
    imageio.mimsave('./exports/' + moviename, frames, fps=fps)
    # Clean up directory
    for filename in filenames:
    	os.remove(filename)

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