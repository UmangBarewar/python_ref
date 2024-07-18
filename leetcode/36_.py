from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to keep track of seen numbers in rows, columns, and 3x3 boxes
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        # Iterate over each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # Skip empty cells represented by '.'
                if board[r][c] == ".":
                    continue
                
                # Check if the current number is already seen in the current row, column, or 3x3 box
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in boxes[(r // 3, c // 3)]):
                    # If the number is already seen, the board is invalid
                    return False
                
                # Mark the current number as seen in the respective row, column, and 3x3 box
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        # If no conflicts are found, the board is valid
        return True
