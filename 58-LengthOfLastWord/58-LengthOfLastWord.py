# Last updated: 9/14/2025, 4:59:18 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        i = len(s)-1

        while i >= 0 and s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length