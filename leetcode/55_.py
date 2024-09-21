from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        n = len(nums)
        
        for i in range(n):
            # If the current index is beyond the maximum reachable, return False
            if i > max_reachable:
                return False
            
            # Update the maximum reachable index
            max_reachable = max(max_reachable, i + nums[i])
            
            # If we've reached or passed the last index, return True
            if max_reachable >= n - 1:
                return True
        
        return False
