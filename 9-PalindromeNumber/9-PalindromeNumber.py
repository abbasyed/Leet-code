class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        res = [digit for digit in str(x)]

        l, r = 0, len(res)-1

        while l < r:
            if res[l] != res[r]:
                return False
            l+=1
            r-=1
        return True