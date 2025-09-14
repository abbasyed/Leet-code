# Last updated: 9/14/2025, 5:07:44 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        result = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in result:
                return [result[diff], i]
            result[nums[i]] = i
        return []
             
        