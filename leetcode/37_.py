from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def solve(self) -> bool:
        empty = self.find_empty()
        if not empty:
            return True  # Board is solved
        row, col = empty

        for num in map(str, range(1, 10)):  # Try numbers '1' to '9'
            if self.is_valid(num, row, col):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'  # Reset the cell (backtrack)

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return None

    def is_valid(self, num: str, row: int, col: int) -> bool:
        # Check the row
        if num in self.board[row]:
            return False
        
        # Check the column
        for i in range(9):
            if self.board[i][col] == num:
                return False
        
        # Check the 3x3 box
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(box_row_start, box_row_start + 3):
            for j in range(box_col_start, box_col_start + 3):
                if self.board[i][j] == num:
                    return False
        
        return True
