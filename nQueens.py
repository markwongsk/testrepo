def nQueens(n):
    board = [[False for i in range(n)] for i in range(n)]
    printBoard(board)

    def nQueens(board, col):
        if col >= n:
            return board
        for row in range(n):
            board[row][col] = True
            if isValid(board):
                maybeAnswer = nQueens(board, col+1)
                if maybeAnswer:
                    return maybeAnswer
            board[row][col] = False
        return None
    return nQueens(board, 0)
    
def isValid(board):
    n = len(board)
    # columns
    for row in range(n):
        queens = 0
        for col in range(n):
            if board[row][col]:
                queens += 1
        if queens > 1:
            return False

    # diagonals
    for row in range(n):
        diagQueens = [0]*4
        for col in range(row+1):
            if board[row - col][col]:
                diagQueens[0] += 1
            if board[n - row + col - 1][n - col - 1]:
                diagQueens[1] += 1
            if board[row - col][n - col - 1]:
                diagQueens[2] += 1
            if board[n - row + col - 1][col]:
                diagQueens[3] += 1
        if not reduce(lambda x, y: x and y, [diagQueen <= 1 for diagQueen in diagQueens], True):
            return False
    return True

def printBoard(board):
    print "---------------"
    for row in board:
        for item in row:
            if item:
                print "Q",
            else:
                print "-",
        print
    print "---------------"
    
if __name__ == "__main__":
    printBoard(nQueens(8))


