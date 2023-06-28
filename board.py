from tile import Tile


class Board:
    """ Display the board and the tiles on it """
    def __init__(self, COLUMNS, ROWS, CELL_SIZE):
        self.COLUMNS = COLUMNS
        self.ROWS = ROWS
        self.CELL = CELL_SIZE

        # Initialize a nested list of 0 sized COLUMNS X ROWS
        m = self.COLUMNS
        n = self.ROWS
        self.table = [[0] * m for i in range(n)]
        # initialize the value of center 4 tiles
        self.table[int(n/2 - 1)][int(m/2 - 1)] = 'white'
        self.table[int(n/2 - 1)][int(m/2)] = 'black'
        self.table[int(n/2)][int(m/2 - 1)] = 'black'
        self.table[int(n/2)][int(m/2)] = 'white'

        # Initialize black and white value
        self.white = 255
        self.black = 0

        # Initialize bla
        # ck and white tile counts on the board
        self.black_count = 0
        self.white_count = 0

        # Initialize two list to store current tiles' position (col, row)
        self.black_tiles = []
        self.white_tiles = []

    def display(self):
        """ Draw the board lines and current tiles """
        # Draw the board lines
        # vertical
        for i in range(1, self.COLUMNS):
            strokeWeight(4)
            line(i * self.CELL, 0, i * self.CELL, self.ROWS * self.CELL)
        # horizontal
        for i in range(1, self.ROWS):
            strokeWeight(4)
            line(0, i * self.CELL, self.COLUMNS * self.CELL, i * self.CELL)

        # Draw current tiles
        # Update color counts and positions
        self.black_count = 0
        self.white_count = 0
        self.black_tiles = []
        self.white_tiles = []
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                if self.table[row][col] != 0:
                    if self.table[row][col] == 'black':
                        color = self.black
                        self.black_count += 1
                        self.black_tiles.append((col, row))
                    elif self.table[row][col] == 'white':
                        color = self.white
                        self.white_count += 1
                        self.white_tiles.append((col, row))
                    tile = Tile(col, row, color, self.CELL)
                    tile.display()
