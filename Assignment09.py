from bangtal import *
from enum import Enum


class State(Enum):
    BLANK = 0
    POSSIBLE = 1
    BLACK = 2
    WHITE = 3


class Turn(Enum):
    BLACK = 1
    WHITE = 2


def setState(x, y, s):
    object = board[x][y]
    object.state = s

    if s == State.BLANK:
        object.setImage("Images/blank.png")
    elif s == State.BLACK:
        object.setImage("Images/black.png")
    elif s == State.WHITE:
        object.setImage("Images/white.png")
    elif s == Turn.BLACK:
        object.setImage("Images/black possible.png")
    else:
        object.setImage("Images/white possible.png")


turn = Turn.BLACK


def stone_onMouseAction(x, y):
    global turn
    if turn == Turn.BLACK:
        setState(x, y, State.BLACK)
        turn = Turn.WHITE
    else:
        setState(x, y, State.WHITE)
        turn = Turn.BLACK

    setPossible()


def setPossible_xy_dir(x, y, dx, dy):
    if turn == Turn.BLACK:
        mine = State.BLACK
        other = State.WHITE
    else:
        mine = State.WHITE
        other = State.BLACK

    possible = True
    while True:
        x = x + dx
        y = y + dy

        object = board[y][x]
        if object.state == other:
            possible = True
        elif object.state == mine:
            return possible
        else:
            return False


def setPossible():
    for x in range(8):
        for y in range(8):
            object = board[x][y]
            if object.state == State.BLACK:
                return
            if object.state == State.WHITE:
                return

            if setPossible_xy_dir(x, y, -1, -1):
                setState(x, y, State.POSSIBLE)
            if setPossible_xy_dir(x, y, -1, 0):
                setState(x, y, State.POSSIBLE)
            if setPossible_xy_dir(x, y, -1, 1):
                setState(x, y, State.POSSIBLE)
            if setPossible_xy_dir(x, y, 0, -1):
                setState(x, y, State.POSSIBLE)
            if setPossible_xy_dir(x, y, 0, 1):
                setState(x, y, State.POSSIBLE)
            if setPossible_xy_dir(x, y, 1, -1):
                setState(x, y, State.POSSIBLE)
            if setPossible_xy_dir(x, y, 1, 0):
                setState(x, y, State.POSSIBLE)
            if setPossible_xy_dir(x, y, 1, 1):
                setState(x, y, State.POSSIBLE)


setGameOption(GameOption.ROOM_TITLE, False)
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("Othello", "Images/background.png")
board = [[] for i in range(8)]

for x in range(8):
    for y in range(8):
        object = Object("Images/blank.png")
        object.locate(scene, 40 + x * 80, 40 + y * 80)
        object.show()
        object.onMouseAction = lambda mx, my, action, ix=x, iy=y: stone_onMouseAction(ix, iy)
        board[x].append(object)

startGame(scene)
