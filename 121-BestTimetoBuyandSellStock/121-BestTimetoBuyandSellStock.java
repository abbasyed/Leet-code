// Last updated: 5/7/2025, 8:08:39 PM
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