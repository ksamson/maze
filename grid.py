from PIL import Image, ImageDraw
from cell import Cell

class Grid():
    def __init__(self, row, col, cell_size=50, image_offset=20):
        self.row = row
        self.col = col
        self.cell_size = cell_size
        self.image_offset = image_offset
        self.grid = self.prepare_grid()

    # TODO
    def __str__(self):
        pass


    # Prepares the grid which contains row*col number of cells
    # the grid is a list which contains the cells
    def prepare_grid(self):
        grid = []
        for x in range(self.row):
            for y in range(self.col):
                grid.append(Cell(x,y,self.cell_size))
        self._set_neighbors(grid)
        return grid


    def _get_index(self, x, y):
        return y + (x * self.col)


    # Helper function which pre-sets the neighbors of each created cell in the grid
    def _set_neighbors(self, grid):
        for cell in grid:
            cell.top = grid[self._get_index(cell.x - 1, cell.y)] if self._valid_index(cell.x - 1, cell.y) else None
            cell.right = grid[self._get_index(cell.x, cell.y + 1)] if self._valid_index(cell.x, cell.y + 1) else None
            cell.bottom = grid[self._get_index(cell.x + 1, cell.y)] if self._valid_index(cell.x + 1, cell.y) else None
            cell.left = grid[self._get_index(cell.x, cell.y - 1)] if self._valid_index(cell.x, cell.y - 1) else None


    # Helper function which checks if the passed index is a valid index (out of bounds checking)
    def _valid_index(self, x, y):
        return False if (x < 0 or y < 0 or x > self.row - 1 or y > self.col - 1) else True


    def draw_grid(self, frame=str(0)):
        x = self.row * self.cell_size
        y = self.col * self.cell_size

        image = Image.new("RGB", (x + 2 * self.image_offset, y + 2 * self.image_offset), (255,255,255))

        # Creates a draw object which can be drawed on
        draw = ImageDraw.Draw(image)
        # draw.rectangle((0,0,imgx, imgy), fill="black")

        for cell in self.grid:
            cell.show(draw, self.image_offset)

        #image.save("grid.PNG", "PNG")
        image.save("./exports/maze"+frame+".png", "PNG")
