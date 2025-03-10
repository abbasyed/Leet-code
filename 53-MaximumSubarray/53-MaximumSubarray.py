class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = nums[0] #sum ending at the current position
        max_sum = nums[0] #max_sum found so far

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum