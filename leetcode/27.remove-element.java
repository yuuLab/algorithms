/*
 * @lc app=leetcode id=27 lang=java
 *
 * [27] Remove Element
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int n : nums) {
            if (n != val) {
                nums[k] = n;
                k++;
            }
        }
        return k;
    }
}
// @lc code=end
