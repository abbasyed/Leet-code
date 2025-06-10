# Last updated: 6/9/2025, 6:52:27 PM
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1

        while left < right:
            curr = numbers[left] + numbers[right]
            print(curr)
            if curr == target:
                return ([left+1, right+1])
            elif curr > target:
                right -= 1
            else:
                left += 1
        return -1