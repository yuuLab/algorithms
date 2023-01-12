/*
 * @lc app=leetcode id=121 lang=java
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int buyprice = Integer.MAX_VALUE;
        int op = 0;
        int pist = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < buyprice) {
                buyprice = prices[i];
            }
            pist = prices[i] - buyprice;
            if (op < pist) {
                op = pist;
            }
        }
        return op;
    }
}
// @lc code=end
