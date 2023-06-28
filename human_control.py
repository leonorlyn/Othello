from player_control import PlayerControl


class HumanControl(PlayerControl):
    """
    Handle the human player's methods:
    Find current vaild positions for black tile
    """
    def __init__(self, board):
        self.board = board
        self.ADD = [-1, 0, 1]

        # initialize a list to store valid positions
        self.vaild_positions = []

    def board_check(self):
        """ Scan the board and process empty cells to vaild check """
        # reset the valid positions
        self.vaild_positions = []
        for col in range(self.board.COLUMNS):
            for row in range(self.board.ROWS):
                # only check empty cells
                if self.board.table[row][col] == 0:
                    self.cell_check(col, row)

    def cell_check(self, col, row):
        """ Check the validation of cell (col, row) """
        # check 8 directions seperately
        for xadd in self.ADD:
            for yadd in self.ADD:
                if not (xadd == 0 and yadd == 0):
                    self.line_check(col, row, xadd, yadd)

    def line_check(self, col, row, xadd, yadd):
        """ Check one direction and update valid position """
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
                if next_value == 'white':
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

        # update valid position
        if (competitor_tiles > 0) and (meet_self is True):
            self.vaild_positions.append((col, row))
