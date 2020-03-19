from typing import List
import copy

class Solution:
    #def convertBoardLeetCode(self, my_board):
    #    leet_board = []
    #    leet_row = ""
    #    for row in my_board:
    #        for char in row:
    #            leet_row += char
    #        leet_board.append(leet_row)
    #    return leet_board

    def isQueenValidAtIdx(self, pos, board):
        row, col = pos
        for letter in board[row]:
            if letter == "Q":
                return False
        for line in board:
            if line[col] == "Q":
                return False
        if self.queenInDiagonal(pos, board):
            return False
        return True

    def queenInDiagonal(self, pos, board):
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
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for i in range(n):
            board.append(["."] * n)
        solutions = []
        self.rec_solveNQueens(board, 0, solutions, 0)
        return solutions
        
    def countQueens(self, board):
        queenCount = 0
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == "Q":
                    queenCount += 1
        return queenCount
        
    def rec_solveNQueens(self, board, index, solutions, queens_count):
        if queens_count == len(board):
            if board not in solutions:
                solutions.append(copy.deepcopy(board))
            return
        if index >= len(board[0])**2:
            return

        # try all possible next queen positions
        offset = 0
        while index < len(board)**2 - 1:
            row = index // len(board[0])
            col = index % len(board[0])
            
            if self.isQueenValidAtIdx([row, col], board):
                board[row][col] = "Q"
                queens_count += 1
                self.rec_solveNQueens(board, index + 1, solutions, queens_count)
                board[row][col] = "."
                queens_count -= 1
            else:
                self.rec_solveNQueens(board, index + 1, solutions, queens_count)
            index += 1


def main():
    solution = Solution()
    n = 5
    my_result = solution.solveNQueens(n)
    print(my_result)

main()