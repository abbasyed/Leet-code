class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Sort dictionary items by value (frequency) in descending order
        # and get top k elements
        return [num for num, count in sorted(freq.items(), 
                                          key=lambda x: x[1], 
                                          reverse=True)[:k]]