# Last updated: 5/30/2025, 8:07:49 PM
class Solution(object):
    def checkInclusion(self, s1, s2):
        from collections import Counter
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
    

        len_s1 = len(s1)
        s1_count = Counter(s1)

        for i in range(len(s2) - len_s1 + 1):
            window = s2[i:i + len_s1]
            if Counter(window) == s1_count:
                return True
        return False