def convertBoardLeetCode(my_boards):
        leet_boards = []
        for board in my_boards:
            leet_board = []
            leet_row = ""
            for row in board:
                for char in row:
                    leet_row += char
                leet_board.append(leet_row)
                leet_row = ""
            leet_boards.append(leet_board)
        return leet_boards

def isQueenValidAtIdx(pos, board):
    row, col = pos
    for letter in board[row]:
        if letter == "Q":
            return False
    for line in board:
        if line[col] == "Q":
            return False
    if queenInDiagonal(pos, board):
        return False
    return True

def queenInDiagonal(pos, board):
    row, col = pos
    #check up right
    while row >= 0 and col <= len(board)-1:
        if board[row][col] == "Q":
            return True
        row -= 1
        col += 1
    row, col = pos
    #check down right
    while row <= len(board)-1 and col <= len(board)-1:
        if board[row][col] == "Q":
            return True
        row += 1
        col += 1
    row, col = pos
    #check down left
    while row <= len(board)-1 and col >= 0:
        if board[row][col] == "Q":
            return True
        row += 1
        col -= 1
    row, col = pos
    #check up left
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return True
        row -= 1
        col -= 1

    return False

def countQueens(board):
    print("debug only: you should not need this!")
    queenCount = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                queenCount += 1
    return queenCount