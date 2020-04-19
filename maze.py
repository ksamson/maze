from PIL import Image, ImageDraw


# height and size of the image in pixels
imgx = 500; imgy = 500

# size of a cell block
csize = 50

# Iterates over an image, generating a cell and appending it to a list. Returns the list
def generate_cells():
    cells = []
    rows = imgx // csize
    cols = imgy // csize
    for x in range(rows):
        for y in range(cols):
            cells.append(Cell(x,y))

    return cells


def draw_grid(grid):

    image = Image.new("RGB", (imgx, imgy), (255,255,255))
    # Draw the image
    draw = ImageDraw.Draw(image)
    #draw.rectangle((0,0,imgx, imgy), fill="black")

	#draw.line((0,0), (50,50))
    
    
    for cell in grid:
        # cell arithmetics below:
        # x : row, y : col
        #
        # (x,y)        (x+1, y)
        #     o--------o
        #     |        |
        #     |  Cell  |
        #     |        |
        #     o--------o
        # (x,y+1)      (x+1, y+1)

        x1 = cell.x * csize
        y1 = cell.y * csize
        x2 = (cell.x + 1) * csize
        y2 = (cell.y + 1) * csize

        # top line
        if cell.walls[0]:
            draw.line((x1, y1, x2, y1), (0,250,0))
        # right line
        if cell.walls[1]:
            draw.line((x2, y1, x2, y2), (0,250,0))
        # bottom line
        if cell.walls[2]:
            draw.line((x2, y2, x1, y2), (250,0,0))
        # left line
        if cell.walls[3]:
            draw.line((x1, y2, x1, y1), (0,0, 250))

    image.save("test.PNG", "PNG")

def main():
    grid = generate_cells()
    draw_grid(grid)

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # A boolean list which checks if a cell has a 'wall' around them
        # walls = [Top wall, Right wall, Bottom wall, Left wall]
        self.walls = [False, False, True, False]

if __name__ == "__main__":
    main()
