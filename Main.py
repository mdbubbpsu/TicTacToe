import copy

def createBoard(rows, cols):
    board = [[False for i in range(cols)] for j in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(cols):
            if count < rows * cols:
                board[i][j] = count
                count += 1
            else:
                board[i][j] = 9
    return ticTacToe(board)


class ticTacToe(object):

    def __init__(self, board):
        self.board = board
        self.x = len(board)
        self.y = len(board[0])

    def getBoard(self):
        return self.board

    def solved(self):
        db = self.board
        one = [self.board[0][0], self.board[1][0], self.board[2][0]]
        two = [self.board[0][1], self.board[1][1], self.board[2][1]]
        three = [self.board[0][2], self.board[1][2], self.board[2][2]]

        four = [self.board[0][0], self.board[0][1], self.board[0][2]]
        five = [self.board[1][0], self.board[1][1], self.board[1][2]]
        six = [self.board[2][0], self.board[2][1], self.board[2][2]]

        seven = [self.board[0][0], self.board[1][1], self.board[2][2]]
        eight = [self.board[0][2], self.board[1][1], self.board[2][0]]
        # First column
        if self.board[0][0] != 1 and self.board[1][0] != 4 and self.board[2][0] != 7:
            if all(i == 'X' for i in one):
                return True, 'X'
            elif all(i == 'O' for i in one):
                return True, 'O'
            else:
                return False, -1

        # Second column
        elif self.board[0][1] != 2 and self.board[1][1] != 5 and self.board[2][1] != 8:
            if all(i == 'X' for i in two):
                return True, 'X'
            elif all(i == 'O' for i in two):
                return True, 'O'
            else:
                return False, -1

        # Third Column
        elif self.board[0][2] != 3 and self.board[1][2] != 6 and self.board[2][2] != 9:
            if all(i == 'X' for i in three):
                return True, 'X'
            elif all(i == 'O' for i in three):
                return True, 'O'
            else:
                return False, -1

        # First Row
        elif self.board[0][0] != 1 and self.board[0][1] != 2 and self.board[0][2] != 3:
            if all(i == 'X' for i in four):
                return True, 'X'
            elif all(i == 'O' for i in four):
                return True, 'O'
            else:
                return False, -1

        # Second Row
        elif self.board[1][0] != 4 and self.board[1][1] != 5 and self.board[1][2] != 6:
            if all(i == 'X' for i in five):
                return True, 'X'
            elif all(i == 'O' for i in five):
                return True, 'O'
            else:
                return False, -1

        # Third Row
        elif self.board[2][0] != 7 and self.board[2][1] != 8 and self.board[2][2] != 9:
            if all(i == 'X' for i in six):
                return True, 'X'
            elif all(i == 'O' for i in six):
                return True, 'O'
            else:
                return False, -1

        # First diagonal
        elif self.board[0][0] != 1 and self.board[1][1] != 5 and self.board[2][2] != 9:
            if all(i == 'X' for i in seven):
                return True, 'X'
            elif all(i == 'O' for i in seven):
                return True, 'O'
            else:
                return False, -1

        # Second diagonal
        elif self.board[0][2] != 3 and self.board[1][1] != 5 and self.board[2][0] != 7:
            if all(i == 'X' for i in eight):
                return True, 'X'
            elif all(i == 'O' for i in eight):
                return True, 'O'
            else:
                return False, -1
        else:
            return False, -1

    def displayBoard(self, board):
        for i in range(self.x):
            for j in range(self.y):
                if j == 0:
                    print("|", board[i][j], " | ", end="")
                else:
                    print(board[i][j], " | ", end="")
            print()

    def valid(self, row, col):
        if self.board[row][col] != 'X' and self.board[row][col] != 'O':
            return True
        else:
            return False

    def performMove(self, row, col, turn):
        if self.valid(row, col):
            self.board[row][col] = turn
            self.displayBoard(self.board)
            return True
        else:
            print("INVALID MOVE, PLEASE TRY AGAIN")
            self.displayBoard(self.board)
            return False

    def copy(self):
        return ticTacToe(copy.deepcopy(self.board))

    def successors(self, turn):
        for i in range(self.x):
            for j in range(self.y):
                copyBoard = self.copy()
                if copyBoard.performMove(i, j, turn):
                    yield (i, j), copyBoard

    def get_best_move(self, board):
        startBoard = self
        value, move = self.maxValue(startBoard)
        return value, move

    def maxValue(self, board):
        boo, turn = board.solved()
        util = 0
        if boo:
            if turn == 'X':
                util = -1
            elif turn == 'O':
                util = 1
            return util, None
        v = -1000
        returnIndex = (0, 0)
        for ind, newBoard in board.successors('O'):
            v2, a2 = self.minValue(newBoard)
            if v2 > v:
                v, returnIndex = v2, ind
        return v, returnIndex


    def minValue(self, board):
        boo, turn = board.solved()
        util = 0
        if boo:
            if turn == 'X':
                util = 1
            elif turn == 'O':
                util = -1
            return util, None
        v = 1000
        returnIndex = (0, 0)
        for ind, newBoard in board.successors('X'):
            v2, a2 = self.maxValue(newBoard)
            if v2 < v:
                v, returnIndex = v2, ind
        return v, returnIndex


b = createBoard(3,3)
#b.displayBoard(b.getBoard())
print(b.get_best_move(b))



























