class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    #helper function
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
        ord("a") <= ord(c) <= ord("z") or 
        ord("0") <= ord(c) <= ord("9"))