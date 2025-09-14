# Last updated: 9/14/2025, 4:58:15 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    print(i)
        return None
             
        