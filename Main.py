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
        self.scoresDict = {}

    def start(self):
        i = 0

        dict = {}
        compDict = {}
        count = 1
        for i in range(self.x):
            for j in range(self.y):
                dict[count] = (i,j)
                compDict[(i,j)] = count
                count += 1

        while not self.solved()[0]:
            self.displayBoard()
            move = int(input("Please enter which spot you would like to move in: "))
            valid = self.valid(dict[move][0], dict[move][1])
            while not valid:
                self.displayBoard()
                move = int(input("Invalid move please pick again: "))
                valid = self.valid(dict[move][0], dict[move][1])
            self.performMove(dict[move][0], dict[move][1], 'X')
            util, move = self.get_best_move()
            if move is not None:
                self.performMove2(move[0], move[1], 'O')
                print("Computer moved into spot: ",compDict[move])
                if self.solved()[0]:
                    print("GAME OVER, O wins")
                    self.displayBoard()
                    break
            else:
                print("GAME OVER, it's a tie!")
                break


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
        return type(self.board[row][col]) == int


    def performMove(self, row, col, turn):
        self.board[row][col] = turn
        self.displayBoard()


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


    def maxValue(self, visited, alpha, beta, depth):
        boo, turn = self.solved()
        if self.draw() and not boo:
            return 0, None
        elif boo:
            return -1, None
        localMax = -1000
        returnIndex = (None, None)
        for ind, newBoard in self.successors2('O'):
            childScore, a2 = newBoard.minValue(visited, alpha, beta, depth + 1)
            if childScore > localMax:
                localMax, returnIndex = childScore, ind
                alpha = max(alpha, childScore)
            #print("     max value at depth", depth, "for child", newBoard.getBoard(), " is ", localMax, "")
            if localMax >= beta:
                return localMax, returnIndex

        #print("Max value at depth", depth, "for parent" ,self.getBoard(),"is", localMax, returnIndex, alpha)

        return localMax, returnIndex

    def minValue(self, visited, alpha, beta, depth):
        boo, turn = self.solved()
        if self.draw() and not boo:
            return 0, None
        elif boo:
            return 1, None
        localMin = 1000
        returnIndex = (0, 0)
        for ind, newBoard in self.successors2('X'):
            childScore, a2 = newBoard.maxValue(visited, alpha, beta, depth + 1)
            if childScore < localMin:
                localMin, returnIndex = childScore, ind
                beta = min(beta, localMin)
            #print("     min value at depth", depth, "for child", newBoard.getBoard(), " is ", localMin, "")
            if localMin <= alpha:
                return localMin, returnIndex
        #print("Overall Min value at depth", depth, "for parent" ,self.getBoard(),"is", localMin, returnIndex, beta)
        return localMin, returnIndex


b = createBoard(2,2)
c = ticTacToe([['X', 2, 3], [4, 5, 6], [7,8,9]])
d = ticTacToe([['X', 'X', 'O'], ['O', 'X', 6], [7,8,9]])
e = ticTacToe([[1, 2,3], [4,5,6], [7,8,9]])

#c.displayBoard(c.getBoard())
e.start()
#e.displayBoard()
#print(e.get_best_move())
#print(e.scoresDict.items())



























