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

def placeMove(number):
    rowNum = number //3
    colNum = number % 3
    if colNum == 0:
        rowNum -= 1
        colNum = 2
    else:
        colNum -= 1
    if valid(board, rowNum,colNum):
        board[rowNum][colNum] = 'X'
        start = False
        printBoard(start)
        computerMove()
    else:
        print("Invalid move. Please choose again")
        userInput()

def userInput():
    userNum = input(" \nYou are player X please make your first move by typing in the number of the spot you wish to move into \n")
    placeMove(int(userNum))

def valid(lboard, rowNum, colNum):
    if lboard[rowNum][colNum] != 'X' and lboard[rowNum][colNum] != 'O':
        return True
    else:
        return False


def computerMove():
    openSpots = 8
    localBoard = board

    if openSpots == 0:
        #Return max points list
        a = 2
    else:
        print('\n \n \n \n ')
        for localRow in range(0,3):
            for localCol in range(0,3):
                if valid(localBoard, localRow,localCol):
                    localBoard[localRow][localCol] = 'O'
                        #CALL MINIMAX AGAIN
                    print(localBoard[localRow][localCol], "   ", end=" ")
                else:
                    print(localBoard[localRow][localCol], "   ", end=" ")

            print()





def main():
    start = True
    board = printBoard(start)
    userInput()








if __name__ == '__main__':
    main()