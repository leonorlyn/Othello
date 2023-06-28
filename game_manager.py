from player_control import PlayerControl
from human_control import HumanControl
from computer_control import ComputerControl


class GameManager:
    """ Switching players """
    def __init__(self, board):
        self.board = board
        self.pc = PlayerControl(board)
        self.hc = HumanControl(board)
        self.cc = ComputerControl(board)
        # Track whether it's human's turn or not
        self.human_turn = True
        # set a counter
        self.counter = 0

    def human_make_move(self, mouseX, mouseY):
        """ Manage human move """
        col = int(mouseX // self.board.CELL)
        row = int(mouseY // self.board.CELL)
        # Move when it's human's turn
        if self.human_turn:
            # scan current board to update valid positions
            self.hc.board_check()
            # check whether the valid positions exist
            if len(self.hc.vaild_positions) != 0:
                # check whether the cell is empty
                if self.board.table[row][col] == 0:
                    # check whether the cell is valid
                    if (col, row) in self.hc.vaild_positions:
                        # update the new black tile on the board
                        self.board.table[row][col] = 'black'
                        # flip tiles
                        self.pc.flip(col, row, 'black')
                        # set the counter
                        self.counter = 100
                        # switch to computer's turn
                        self.human_turn = False
            else:
                # No valid positions for human, make it computer's turn
                self.human_turn = False

    def computer_make_move(self):
        """ Manage computer move """
        # Move when it's computer's turn
        if not self.human_turn:
            # scan current board to update best position
            self.cc.board_check()
            # check whether best position exists
            if self.cc.best_position != (-1, -1):
                # wait the counter
                if self.counter == 0:
                    # put the white tile one the best position
                    col = self.cc.best_position[0]
                    row = self.cc.best_position[1]
                    self.board.table[row][col] = 'white'
                    # flip tiles
                    self.pc.flip(col, row, 'white')
                    # switch to human's turn
                    self.human_turn = True
            else:
                # No best position means no more valid steps for white
                self.human_turn = True

    def count_down(self):
        self.counter -= 1

    def display_turn(self):
        if self.human_turn:
            message = "Player's turn"
        else:
            message = "Computer's turn"

        textAlign(LEFT)
        textSize(20)
        fill(255, 0, 0)
        text(message, 20, 20)
