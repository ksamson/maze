from PIL import Image, ImageDraw
import random

class Cell():
    def __init__(self, x, y, cell_size=50):
        self.x = x
        self.y = y
        self.size = cell_size
        # A boolean list which checks if a cell has a 'wall' around them
        # walls = [Top wall, Right wall, Bottom wall, Left wall]
        self.walls = [True, True, True, True]
        self.visited = False

    def __str__(self):
        return "Cell Object with coordinate ({},{})".format(self.x, self.y)

    # Check the neighbors of a current cell to see if it has been visited
    # TODO:
    def check_neighbors(self):
        neighbors = []
        # Append to the list if the following cells have been visited for a given cell
        # e.g. if cell(top).visited == True: neighbors.append())
        # top = get_index(row, col-1)
        # right = get_index(row + 1, col)
        # bottom = get_index(row, col+1)
        # left = get_index(row-1,col)
        return neighbors

    # show the cell
    def show(self, draw):
        # cell walls definition below:
        # x : row, y : col
        #
        # (x,y)        (x+1, y)
        #     o--------o
        #     |        |
        #     |  Cell  |
        #     |        |
        #     o--------o
        # (x,y+1)      (x+1, y+1)
        
        x1 = self.x * self.size
        y1 = self.y * self.size
        x2 = (self.x + 1) * self.size
        y2 = (self.y + 1) * self.size

        # top line
        if self.walls[0]:
            draw.line((x1, y1, x2, y1), (0,250,0))
        # right line
        if self.walls[1]:
            draw.line((x2, y1, x2, y2), (0,250,0))
        # bottom line
        if self.walls[2]:
            draw.line((x2, y2, x1, y2), (0,250,0))
        # left line
        if self.walls[3]:
            draw.line((x1, y2, x1, y1), (0,250, 0))

        if self.visited:
            draw.rectangle((x1,y1,x2,y2), fill="violet")