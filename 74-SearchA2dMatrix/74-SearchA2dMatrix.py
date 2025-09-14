# Last updated: 9/14/2025, 4:59:16 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """# brute force
        for r in range(len(matrix)):
            for c in range (len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False"""

        #optimal

        ROWS, COLS = len(matrix), len(matrix[0])
        low, high = 0, ROWS * COLS - 1

        while low <= high:
            mid = low + (high - low) // 2
            rows, cols = mid // COLS, mid % COLS
            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] > target:
                high =  mid - 1
            else:
                low = mid + 1
        return False