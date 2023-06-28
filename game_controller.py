import os


class GameController:
    """Maintains the state of the game."""
    def __init__(self, board, game_manager):
        self.board = board
        self.gm = game_manager
        self.game_over = False
        # Initialize variables for score recording
        self.user_name = ""
        self.recored = False

    def status_check(self):
        # scan the board, check whether vaild steps exist for human
        self.gm.hc.board_check()
        human_valid = self.gm.hc.vaild_positions
        # scan the board, check whether vaild steps exist for human
        self.gm.cc.board_check()
        computer_valid = self.gm.cc.best_position
        # end the game when no valid steps for both player
        if len(human_valid) == 0 and computer_valid == (-1, -1):
            self.game_over = True

    def update(self):
        """Display the board and check if game is over"""
        self.board.display()
        self.gm.display_turn()

        self.status_check()
        if self.game_over:
            self.display_end_text()
            # record the score
            # self.score_check()
            self.record_score()

    def display_end_text(self):
        """ Display end of game message """
        black = self.board.black_count
        white = self.board.white_count
        if black > white:
            message = "You win!  " + str(black) + " to " + str(white)
        elif white > black:
            message = "You lose.  " + str(black) + " to " + str(white)
        else:
            message = "Tie.  " + str(black) + " to " + str(white)
        # Display the result
        center = self.board.ROWS * self.board.CELL / 2

        textAlign(CENTER)
        textSize(40)
        fill(255, 0, 0)
        text(message, center, center)

    def name_record(self, name):
        self.user_name = name

    def record_score(self):
        if not self.recored:
            highest_score = 0
            # obtain current highest record score
            if os.path.getsize("scores.txt") != 0:
                m = open("scores.txt", 'r')
                highest_score = int(m.readline().split()[-1])
                m.close()
            # obtain the user's score
            score = self.board.black_count
            if score > highest_score:
                # record the score on the first line
                with open('scores.txt', 'r+') as f:
                    content = f.read()
                    f.seek(0, 0)
                    f.write(self.user_name + ' ' + str(score) + '\n' + content)
                    f.close()
            else:
                # record on the last line
                with open('scores.txt', 'a') as f:
                    f.write(self.user_name + ' ' + str(score) + '\n')
                    f.close()
            # update record status
            self.recored = True
