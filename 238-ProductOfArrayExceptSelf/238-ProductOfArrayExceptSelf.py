# Last updated: 9/14/2025, 4:59:05 AM
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        """#bruteforce
        n = len(nums)
        res = [0]*n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i==j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res"""

        #optimal:

        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        


        