class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brutefore approach:
        """for i in range(len(nums)-1) :
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:      
                    return [i,j]"""

        # using hashmap dictionary:
        numToIndexMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numToIndexMap:
                return [numToIndexMap[diff], i]
            else: 
                numToIndexMap[nums[i]] = i

        return "null"
        