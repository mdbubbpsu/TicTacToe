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

    def start(self):
        i = 0
        boo, val = self.solved()
        dict = {}
        count = 1
        for i in range(self.x):
            for j in range(self.y):
                dict[count] = (i,j)
                count += 1

        print(dict)
        while not boo:
            print(234)
            if i % 2 == 0:
                self.displayBoard(self.getBoard())
                move = int(input("Please enter which spot you would like to move in: "))
                if self.valid(dict[move][0], dict[move][1]):
                    self.performMove(dict[move][0], dict[move][1], 'X')
                print(self.getBoard())
                print(self.get_best_move(self))
                break


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

    def performMove2(self, row, col, turn):
        if self.valid(row, col):
            self.board[row][col] = turn
            return True
        else:

            return False

    def successors2(self, turn):
        for i in range(self.x):
            for j in range(self.y):
                copyBoard = self.copy()
                if copyBoard.performMove2(i, j, turn):
                    yield (i, j), copyBoard
    def draw(self, board):
        count = 1
        boardRep = board.getBoard()
        for i in range(self.x):
            for j in range(self.y):
                if boardRep[i][j] == count:
                    return False
                count += 1
        return True

    def get_best_move(self, board):
        startBoard = board
        alpha = -1000
        beta = 1000
        value, move = self.maxValue(startBoard, alpha, beta)
        return value, move


# Current problem: something messed up with the pruning. not taking 1 as max when o wins


    def maxValue(self, board, alpha, beta):
        boo, turn = board.solved()
        if self.draw(board):
            print("TIE from min", board.getBoard())
            return 0, None
        elif boo:
            print("X Wins from min", board.getBoard())
            return -1, None
        localMax = -1000
        returnIndex = (None, None)
        print("Parent - X: ", board.getBoard())
        for ind, newBoard in board.successors2('O'):
            print("Child - O", newBoard.getBoard())
            childScore, a2 = self.minValue(newBoard, alpha, beta)
            print( "beta", beta)
            if childScore > localMax:
                localMax, returnIndex = childScore, ind
                alpha = max(alpha, localMax)
            if localMax >= beta:
                return localMax, ind
        return localMax, returnIndex

    def minValue(self, board, alpha, beta):
        boo, turn = board.solved()
        if self.draw(board):
            print("TIE from max", board.getBoard())
            return 0, None
        elif boo:
            db = board.getBoard()
            print("O Wins from max", board.getBoard())
            print("alpha", alpha, "beta", beta)
            return 1, None

        localMin = 1000
        returnIndex = (0, 0)
        for ind, newBoard in board.successors2('X'):

            v2, a2 = self.maxValue(newBoard, alpha, beta)
            print(v2, localMin, "alpha", alpha)
            if v2 < localMin:
                localMin, returnIndex = v2, ind
                beta = min(beta, localMin)
            print(v2, localMin, alpha)
            if localMin <= alpha:
                return localMin, ind
        return localMin, returnIndex


b = createBoard(3, 3)
c = ticTacToe([['X', 2, 3], [4, 5, 6], [7, 8, 9]])
#b.start()
#b.displayBoard(b.getBoard())
print(c.get_best_move(c))



























