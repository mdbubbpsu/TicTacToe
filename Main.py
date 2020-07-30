def printBoard():
    x, y = 3, 3
    board = [[0 for i in range(x)] for j in range(y)]
    count = 1
    print("Game Board: \n")
    for i in range(0, len(board[0])):
        for j in range(0, len(board)):
            board[i][j] = count
            print(board[i][j], "   ", end=" ")
            count += 1
        print()

def main():
    printBoard()







if __name__ == '__main__':
    main()