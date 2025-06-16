# Last updated: 6/15/2025, 7:24:38 PM
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxDiff = -1
        left = 0
        right = 1

        while right < len(nums):
            if nums[right] > nums[left]:
                maxDiff = max(maxDiff, nums[right]-nums[left])
            else:
                left = right
            right += 1
        return maxDiff
            