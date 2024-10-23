def maxsubarray_sum(nums):
  curr_sum=0
  max_sum=float("-inf")
  for num in nums:
    curr_sum+=num
    max_sum=max(max_sum,curr_sum)
    if curr_sum<0:
      curr_sum=0
  return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxsubarray_sum(nums)
