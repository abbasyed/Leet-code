// Last updated: 9/14/2025, 4:59:13 AM
class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int l = 0;
        int r = l + 1;

        while (r < prices.length) {
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                maxP = Math.max(maxP, profit);
            } else {
                l = r;
            }
            r++;
        }
        return maxP;
    }
}