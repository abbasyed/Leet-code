# Last updated: 9/14/2025, 4:58:51 AM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        res = Counter(arr)
        seen = set()

        for v in res.values():
            if v in seen:
                return False
            seen.add(v)
        return True