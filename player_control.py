class PlayerControl:
    """ Handle the method shared by user and computer """
    def __init__(self, board):
        self.board = board
        # Initialize values to reach a cell's neighbors
        self.ADD = [-1, 0, 1]

    def flip(self, col, row, color):
        """
        For the tile at (col, row), flip all possible competitor's tiles
        """
        for xadd in self.ADD:
            for yadd in self.ADD:
                if not (xadd == 0 and yadd == 0):
                    self.one_way(col, row, color, xadd, yadd)

    def one_way(self, col, row, color, xadd, yadd):
        """ Check and flip one direction """
        next_col = col + xadd
        next_row = row + yadd
        # Keep track of number of competitor tiles on the valid way
        competitor_tiles = 0
        # Track whether meet same color on the way
        meet_self = False

        # continuely check validation of tile (next_col, next_row)
        while (next_col >= 0
               and next_row >= 0
               and next_col < self.board.COLUMNS
               and next_row < self.board.ROWS
               ):
            next_value = self.board.table[next_row][next_col]
            # check whether next tile exists
            if next_value != 0:
                # check whether next tile's color is different from 'color'
                if next_value != color:
                    # add 1 to competitor_tiles
                    competitor_tiles += 1
                    # update next_col, next_row for next loop
                    next_col += xadd
                    next_row += yadd
                # when meet same 'color', update and break
                else:
                    meet_self = True
                    break
            # when meet empty cell, break
            else:
                break

        # When the way is valid
        # Flip from the (next_col, next_row) with same 'color'
        if (competitor_tiles > 0) and (meet_self is True):
            # reverse the value of xadd and yadd
            xadd = - xadd
            yadd = - yadd
            # obtain the position of the first tile to flip
            x = next_col + xadd
            y = next_row + yadd
            for i in range(competitor_tiles):
                self.board.table[y][x] = color
                x += xadd
                y += yadd
