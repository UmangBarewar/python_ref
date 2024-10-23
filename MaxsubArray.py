class Solution:
    def maxSubArray(self, nums):
        current_sum = 0  # Initialize the current sum to 0
        max_sum = float('-inf')  # Initialize max_sum to the smallest integer value

        for num in nums:
            current_sum += num  # Add the current number to the current sum
            max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater

            if current_sum < 0:  # If current_sum is negative, reset it to 0
                current_sum = 0

        return max_sum  # Return the maximum sum found

# Example usage
solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = solution.maxSubArray(nums)
print(result)  # Output: 6
