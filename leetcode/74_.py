class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in matrix:
            for sl in l:
                if sl == target:
                    return True
        return False
        
