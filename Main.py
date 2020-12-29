import copy
from collections import defaultdict

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
        self.scoresDict = {}

    def start(self):
        i = 0

        dict = {}
        count = 1
        for i in range(self.x):
            for j in range(self.y):
                dict[count] = (i,j)
                count += 1

        while self.solved():
            print(234)
            if i % 2 == 0:
                self.displayBoard()
                move = int(input("Please enter which spot you would like to move in: "))
                if self.valid(dict[move][0], dict[move][1]):
                    self.performMove(dict[move][0], dict[move][1], 'X')
                print(self.getBoard())
                util, move = self.get_best_move()
                if move is not None:
                    print(util, move)
                    self.performMove2(move[0], move[1], 'O')
                    if not self.solved():
                        print("O wins")
                        print(self.displayBoard())
                        break
                    print(self.displayBoard())
                else:
                    print("GAME OVER")
                    break

                i += 2



    def getBoard(self):
        return self.board

    def solved(self):
        board = self.getBoard()
        one = [board[0][0], board[1][0], board[2][0]]
        two = [board[0][1], board[1][1], board[2][1]]
        three = [board[0][2], board[1][2], board[2][2]]

        four = [board[0][0], board[0][1], board[0][2]]
        five = [board[1][0], board[1][1], board[1][2]]
        six = [board[2][0], board[2][1], board[2][2]]

        seven = [board[0][0], board[1][1], board[2][2]]
        eight = [board[0][2], board[1][1], board[2][0]]
        # First column
        if board[0][0] != 1 and board[1][0] != 4 and board[2][0] != 7:

            if all(i == one[0] for i in one) and one[0] == 'X':
                return True, 'X'
            elif all(i == one[0] for i in one) and one[0] == 'O':
                return True, 'O'


        # Second column
        if board[0][1] != 2 and board[1][1] != 5 and board[2][1] != 8:
            if all(i == two[0] for i in two) and two[0] == 'X':
                return True, 'X'
            elif all(i == two[0] for i in two) and two[0] == 'O':
                return True, 'O'

        # Third Column
        if board[0][2] != 3 and board[1][2] != 6 and board[2][2] != 9:
            if all(i == three[0] for i in three)  and three[0] == 'X':
                return True, 'X'
            elif all(i == three[0] for i in three)  and three[0] == 'O':
                return True, 'O'


        # First Row
        if board[0][0] != 1 and board[0][1] != 2 and board[0][2] != 3:
            if all(i == four[0] for i in four) and four[0] == 'X':
                return True, 'X'
            elif all(i == four[0] for i in four) and four[0] == 'O':
                return True, 'O'

        # Second Row
        if board[1][0] != 4 and board[1][1] != 5 and board[1][2] != 6:
            if all(i == five[0] for i in five) and five[0] == 'X':
                return True, 'X'
            elif all(i == five[0] for i in five) and five[0] == 'O':
                return True, 'O'


        # Third Row
        if board[2][0] != 7 and board[2][1] != 8 and board[2][2] != 9:
            if all(i == six[0] for i in six) and six[0] == 'X':
                return True, 'X'
            elif all(i == six[0] for i in six) and six[0] == 'O':
                return True, 'O'


        # First diagonal
        if board[0][0] != 1 and board[1][1] != 5 and board[2][2] != 9:
            if all(i == seven[0] for i in seven) and seven[0] == 'X':
                return True, 'X'
            elif all(i == seven[0] for i in seven) and seven[0] == 'O':
                return True, 'O'


        # Second diagonal
        if board[0][2] != 3 and board[1][1] != 5 and board[2][0] != 7:
            if all(i == eight[0]  for i in eight) and eight[0] == 'X':
                return True, 'X'
            elif all(i == eight[0] for i in eight) and eight[0] == 'O':
                return True, 'O'
        return False, -1

    def displayBoard(self):
        for i in range(self.x):
            for j in range(self.y):
                if j == 0:
                    print("|", self.getBoard()[i][j], " | ", end="")
                else:
                    print(self.getBoard()[i][j], " | ", end="")
            print()

    def valid(self, row, col):
        if self.board[row][col] != 'X' and self.board[row][col] != 'O':
            return True
        else:
            return False

    def performMove(self, row, col, turn):
        if self.valid(row, col):
            self.board[row][col] = turn
            self.displayBoard()
            return True
        else:
            print("INVALID MOVE, PLEASE TRY AGAIN")
            self.displayBoard()
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
    def draw(self):
        count = 1
        boardRep = self.getBoard()
        falseLst = 0
        for i in range(self.x):
            for j in range(self.y):
                if boardRep[i][j] != count:
                    falseLst += 1
                count += 1

        return falseLst == 9

    def get_best_move(self):
        board = self.getBoard()
        visited = []
        value, move = self.maxValue(visited, -1000, 1000, 0)
        return value, move


# Current problem: something messed up with the pruning. not taking 1 as max when o wins


    def maxValue(self, visited, alpha, beta, depth):
        boo, turn = self.solved()
        if self.draw() and not boo:
            return 0, None
        elif boo:
            return -1, None
        v = -1000
        returnIndex = (None, None)
        for ind, newBoard in self.successors2('O'):
            v2, a2 = newBoard.minValue(visited, alpha, beta, depth + 1)
            if v2 > v:
                v, returnIndex = v2, ind
                alpha = max(alpha, v)
            print("     max value at depth", depth, "for child", newBoard.getBoard(), " is ", v, "")
            if v >= beta:
                return v, returnIndex

        print("Max value at depth", depth, "for parent" ,self.getBoard(),"is", v, returnIndex, alpha)

        return v, returnIndex

    def minValue(self, visited, alpha, beta, depth):
        boo, turn = self.solved()
        if self.draw() and not boo:
            return 0, None
        elif boo:
            return 1, None
        v = 1000
        returnIndex = (0, 0)
        for ind, newBoard in self.successors2('X'):
            v2, a2 = newBoard.maxValue(visited, alpha, beta, depth + 1)
            if v2 < v:
                v, returnIndex = v2, ind
                beta = min(beta, v)
            print("     min value at depth", depth, "for child", newBoard.getBoard(), " is ", v, "")
            if v <= alpha:
                return v, returnIndex
        print("Overall Min value at depth", depth, "for parent" ,self.getBoard(),"is", v, returnIndex, beta)
        return v, returnIndex


b = createBoard(2,2)
c = ticTacToe([[1, 2, 3], [4, 5, 6], [7,8,9]])
d = ticTacToe([['X', 'X', 'O'], ['O', 'X', 6], [7,8,9]])
e = ticTacToe([[1, 2,3], [4,5,6], [7,8,9]])

#c.displayBoard(c.getBoard())
e.start()
#e.displayBoard()
#print(e.get_best_move())
#print(e.scoresDict.items())



























