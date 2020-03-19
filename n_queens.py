from typing import List

class Solution:
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
        print("start")
        board = []
        for i in range(n):
            board.append(["."] * n)
        print(board)
        solutions = []
        self.rec_solveNQueens(board, 0, solutions, 0)
        return solutions
        
    def rec_solveNQueens(self, board, index, solutions, queens_count):
        if queens_count == len(board):
            solutions.append(board)
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
    n = 4
    solutions = solution.solveNQueens(n)
    print(solutions)

main()