class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # brute force
        for r in range(len(matrix)):
            for c in range (len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False