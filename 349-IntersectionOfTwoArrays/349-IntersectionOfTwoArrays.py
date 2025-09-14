# Last updated: 9/14/2025, 4:58:59 AM
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        intersection = nums1_set.intersection(nums2_set)

        return list(intersection)
