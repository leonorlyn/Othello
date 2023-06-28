from player_control import PlayerControl


class ComputerControl(PlayerControl):
    """
    Handle the computer player's methods:
    Find best position for whitle tile
    """
    def __init__(self, board):
        self.board = board
        self.ADD = [-1, 0, 1]

        # initialize a best position for computer
        self.best_position = (-1, -1)

    def board_check(self):
        """ Scan the board and process empty cells to vaild check """
        # reset the best position
        self.best_position = (-1, -1)
        # keep track of the maximum possible flips
        best_flips = 0
        for col in range(self.board.COLUMNS):
            for row in range(self.board.ROWS):
                # only check empty cells
                if self.board.table[row][col] == 0:
                    possible_flips = self.cell_check(col, row)
                    # if possible_flips is higher than before
                    if possible_flips > best_flips:
                        # update the best position and best_flips
                        self.best_position = (col, row)
                        best_flips = possible_flips

    def cell_check(self, col, row):
        """
        Check the validation of cell (col, row), return total flips
        Values -> Value
        """
        # Store total possible flips on all directions
        total_flips = 0
        # check 8 directions seperately
        for xadd in self.ADD:
            for yadd in self.ADD:
                if not (xadd == 0 and yadd == 0):
                    line_flip = self.line_check(col, row, xadd, yadd)
                    if line_flip is not None:
                        total_flips += line_flip
        return total_flips

    def line_check(self, col, row, xadd, yadd):
        """
        Check one direction; if valid, return # of black tiles can be flipped
        Values -> Value or None
        """
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
                # check whether next tile's color is white
                if next_value == 'black':
                    # add 1 to competitor_tiles
                    competitor_tiles += 1
                    # update next_col, next_row for next loop
                    next_col += xadd
                    next_row += yadd
                # when meet black tile, update and break
                else:
                    meet_self = True
                    break
            # when meet empty cell, break
            else:
                break

        # return competitor_tiles when the line is valid
        if (competitor_tiles > 0) and (meet_self is True):
            return competitor_tiles
