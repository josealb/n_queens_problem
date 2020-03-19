from typing import List
import copy

from n_queens_helpers import convertBoardLeetCode, isQueenValidAtIdx, queenInDiagonal, countQueens

class Solution:    
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        board = []
        for i in range(n):
            board.append(["."] * n)
        solutions = []
        self.rec_solveNQueens(board, 0, solutions, 0)
        return convertBoardLeetCode(solutions)
        
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
            
            if isQueenValidAtIdx([row, col], board):
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
    my_result = solution.solveNQueens(n)
    print(my_result)

main()