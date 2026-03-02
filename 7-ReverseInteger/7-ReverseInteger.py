# Last updated: 3/1/2026, 11:45:06 PM
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before multiplying/appending digit
            if result > (INT_MAX - digit) // 10:
                return 0  # overflow

            result = result * 10 + digit

        return sign * result