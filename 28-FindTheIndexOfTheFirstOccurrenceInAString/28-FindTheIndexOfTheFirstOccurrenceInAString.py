# Last updated: 9/14/2025, 4:59:23 AM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        m = len(haystack)
        n = len(needle)

        if n > m:
            return -1

        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1   
