# Last updated: 5/30/2025, 8:19:32 PM
class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import Counter
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
    
        s1_count = Counter(s1)

        for i in range(len(s2)-len(s1) + 1):
            window = s2[i: i + len(s1)]
            if Counter(window) == s1_count:
                return True
        return False