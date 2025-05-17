# Last updated: 5/17/2025, 10:45:43 AM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        resMap = {}
        l = 0;
        maxCount = 0

        for r in range(len(s)):
            if s[r] in resMap:
                l = max(resMap[s[r]] + 1, l)
            resMap[s[r]] = r
            maxCount = max(maxCount, r - l + 1)
        return maxCount