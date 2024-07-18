class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the list to make it easier to avoid duplicates
        n = len(nums)
        result = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # Skip duplicate values
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # Skip duplicate values
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
