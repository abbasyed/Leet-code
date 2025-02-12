class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flattened_list = [item for sublist in matrix for item in sublist]

        for i in flattened_list:
            if target in flattened_list:
                return True
            return False