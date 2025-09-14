# Last updated: 9/14/2025, 4:58:50 AM
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
            