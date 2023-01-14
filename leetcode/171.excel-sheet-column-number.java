/*
 * @lc app=leetcode id=171 lang=java
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
class Solution {
    public int titleToNumber(String columnTitle) {
        int ans = 0;
        int cnt = 0;
        for (int i = columnTitle.length() - 1; i >= 0; i--) {
            // (int) 'A' = 65
            // (int) 'B' = 64 ...
            int num = (int) columnTitle.charAt(i) - 64;
            ans += num * Math.pow(26, cnt);
        }
        return ans;
    }
}
// @lc code=end
