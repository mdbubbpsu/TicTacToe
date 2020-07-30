x, y = 3, 3
board = [[0 for i in range(x)] for j in range(y)]
def printBoard( start):
    count = 1
    print("Welcome to Tic Tac Toe! Here is your game board: \n")
    for i in range(0, len(board[0])):
        for j in range(0, len(board)):
            if start:
                board[i][j] = count
                print(board[i][j], "   ", end=" ")
                count += 1
            if not start:
                print(board[i][j], "   ", end=" ")
        print()
    return board

def placeMove(number,board):
    rowNum = number //3
    colNum = number % 3
    if colNum == 0:
        rowNum -= 1
        colNum = 2
    else:
        colNum -= 1
    board[rowNum][colNum] = 'X'
    start = False
    printBoard(start)

def userInput(board):
    userNum = input(" \nYou are player X please make your first move by typing in the number of the spot you wish to move into \n")
    placeMove(int(userNum),board)

def main():
    start = True
    board = printBoard(start)
    userInput(board)








if __name__ == '__main__':
    main()