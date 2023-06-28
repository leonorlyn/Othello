class Tile:
    """A tile"""
    def __init__(self, column, row, color, CELL_SIZE):
        self.column = column
        self.row = row
        self.color = color
        self.CELL_SIZE = CELL_SIZE

    def display(self):
        """ Draw the tile"""
        fill(self.color)
        tile_x = self.column * self.CELL_SIZE + self.CELL_SIZE / 2
        tile_y = self.row * self.CELL_SIZE + self.CELL_SIZE / 2
        ellipse(tile_x, tile_y, 90, 90)
