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
    def get_unvisited_neighbor(self):
        neighbors = []
        # Append to the list if the following cells have been visited for a given cell
        # e.g. if cell(top).visited == True: neighbors.append())
        if self.top != None and self.top.visited != True:
            neighbors.append(self.top)
        if self.right != None and self.right.visited != True:
            neighbors.append(self.right)
        if self.bottom != None and self.bottom.visited != True:
            neighbors.append(self.bottom)
        if self.left != None and self.left.visited != True:
            neighbors.append(self.left)
        # return random.choice(neighbors) if neighbors else None
        return neighbors

    def check_neighbors(self):
        return True if self.top != None or self.right != None or self.bottom != None or self.left != None else False

    def remove_wall(self, neighbor_cell):
        # current cell's top neighbor
        if self.x - neighbor_cell.x == -1:
            self.walls[1] = False
            neighbor_cell.walls[3] = False            
        
        # current cell's bottom neighbor
        elif self.x - neighbor_cell.x == 1:
            self.walls[3] = False
            neighbor_cell.walls[1] = False

        # current cell's right neighbor
        if self.y - neighbor_cell.y == 1:
            self.walls[0] = False
            neighbor_cell.walls[2] = False

        # current cell's left neighbor
        elif self.y - neighbor_cell.y == -1:
            self.walls[2] = False
            neighbor_cell.walls[0] = False

    # show the cell
    def show(self, draw, image_offset=20):
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
        
        x1 = self.x * self.size + image_offset
        y1 = self.y * self.size + image_offset
        x2 = (self.x + 1) * self.size + image_offset
        y2 = (self.y + 1) * self.size + image_offset

        if self.visited:
            draw.rectangle((x1,y1,x2,y2), fill=(240,240,20,10))

        # top line
        if self.walls[0]:
            draw.line((x1, y1, x2, y1), (0,0,250))
        # right line
        if self.walls[1]:
            draw.line((x2, y1, x2, y2), (0,0,250))
        # bottom line
        if self.walls[2]:
            draw.line((x2, y2, x1, y2), (0,0,250))
        # left line
        if self.walls[3]:
            draw.line((x1, y2, x1, y1), (0,0,250))
