class Solution:
    def romanToInt(self, s: str) -> int:
        
        resMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        
        res= 0
        prev_value = 0
        for c in reversed(s):
            curr_value = resMap[c]
            if prev_value > curr_value:
                res -= curr_value
            else:
                res += curr_value
            prev_value = curr_value
        return res