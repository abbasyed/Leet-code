# Last updated: 3/23/2025, 2:06:04 AM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        """seen = set()
        # TC = O(n), SC = O(n)
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1"""

    # optimal

        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
    
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
    
        return slow