# Last updated: 5/20/2025, 3:32:17 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = nums1+nums2
        res.sort()

        length = len(nums1)+len(nums2)
        if length % 2 == 0:
            return (res[length // 2 - 1] + res[length // 2]) / 2.0
            
        else:
            return res[length // 2]

            