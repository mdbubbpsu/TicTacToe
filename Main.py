def printBoard():
    x, y = 3, 3
    board = [[0 for i in range(x)] for j in range(y)]
    count = 1
    print("Welcome to Tic Tac Toe! Here is your game board: \n")
    for i in range(0, len(board[0])):
        for j in range(0, len(board)):
            board[i][j] = count
            print(board[i][j], "   ", end=" ")
            count += 1
        print()


def userInput():
    userNum = input(" \nYou are player X please make your first move by typing in the number of the spot you wish to move into \n")
    print(userNum)

def main():
    printBoard()
    userInput()








if __name__ == '__main__':
    main()