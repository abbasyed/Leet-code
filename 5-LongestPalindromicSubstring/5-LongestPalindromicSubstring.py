# Last updated: 7/14/2025, 2:18:47 AM
class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        result = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(len(s)):
            temp1 = expand(i, i)
            temp2 = expand(i, i+1)

            if len(temp1) > len(result):
                result = temp1
            if len(temp2) > len(result):
                result = temp2

        return result