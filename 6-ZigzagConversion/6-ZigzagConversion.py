# Last updated: 7/15/2025, 6:41:13 PM
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]
        
        # Check if sorted in ascending order
            is_sorted = all(window[j] < window[j+1] for j in range(k - 1))
        
        # Check if all elements are consecutive
            is_consecutive = max(window) - min(window) == k - 1 and len(set(window)) == k
        
            if is_sorted and is_consecutive:
                result.append(max(window))
            else:
                result.append(-1)
    
        return result