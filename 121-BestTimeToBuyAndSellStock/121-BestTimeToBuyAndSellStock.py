# Last updated: 3/1/2026, 11:44:48 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxPrice = 0
        minPrice = float('inf')
        
        for price in prices:
            if(price < minPrice):
                minPrice = price
            
            else:
                currentPrice = price - minPrice

                if(currentPrice>maxPrice):
                    maxPrice = currentPrice

        return maxPrice