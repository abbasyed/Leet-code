# Last updated: 9/14/2025, 5:10:17 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        result = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in result:
                return [result[diff], i]
            result[num] = i
        return []        
        