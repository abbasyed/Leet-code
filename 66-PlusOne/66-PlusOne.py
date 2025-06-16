# Last updated: 6/15/2025, 7:34:35 PM
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int("".join(map(str, digits)))
        number += 1
        return [int(digit) for digit in str(number)]