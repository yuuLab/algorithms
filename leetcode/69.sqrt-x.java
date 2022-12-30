/*
 * @lc app=leetcode id=69 lang=java
 *
 * [69] Sqrt(x)
 */

// @lc code=start
class Solution {
    public int mySqrt(int x) {
        if (x == 0)
            return 0;

        int result = 1;
        while (result <= x / result) {
            result += 1;
        }
        return result - 1;
    }
}
// @lc code=end
