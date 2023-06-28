from board import Board
from game_manager import GameManager
from game_controller import GameController


COLUMNS = 8
ROWS = 8
CELL_SIZE = 100


bd = Board(COLUMNS, ROWS, CELL_SIZE)
gm = GameManager(bd)
gc = GameController(bd, gm)


def setup():
    size(CELL_SIZE * COLUMNS, CELL_SIZE * ROWS)

    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
        gc.name_record(answer)


def draw():
    background(0, 105, 0)
    if gm.counter > 0:
        gm.count_down()
    gm.computer_make_move()
    gc.update()


def mousePressed():
    gm.human_make_move(mouseX, mouseY)


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
