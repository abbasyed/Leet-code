class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    # create a hashmap count to store number and it frequencies
        count = {}
      # create a empty indices frequency including the last position of the nums
        freq = [[] for i in range(len(nums)+1)]

        # append count hashmap with num and frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # update frequencies array
        for num, val in count.items():
            freq[val].append(num)

        # return result by moving from -1 index

        res = []
        for i in range(len(freq)-1, 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
