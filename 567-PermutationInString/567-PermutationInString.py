# Last updated: 9/14/2025, 4:58:56 AM
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