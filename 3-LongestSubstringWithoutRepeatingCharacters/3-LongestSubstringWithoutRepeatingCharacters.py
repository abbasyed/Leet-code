# Last updated: 5/20/2025, 3:06:53 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        resMap = {}
        maxCount = 0
        l = 0

        for r in range(len(s)):
            if s[r] in resMap:
                l = max(l, resMap[s[r]]+1)
            resMap[s[r]] = r
            maxCount = max(maxCount, r - l+1)
        return maxCount