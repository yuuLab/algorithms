/*
 * @lc app=leetcode id=11 lang=java
 *
 * [11] Container With Most Water
 */

// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        int area = -1;
        int start = 0;
        int end = height.length - 1;
        while (start < end) {
            int leftHeight = height[start];
            int rightHeight = height[end];

            area = Math.max(area, (end - start) * Math.min(leftHeight, rightHeight));
            if (leftHeight > rightHeight) {
                end--;
            } else {
                start++;
            }
        }
        return area;
    }
}
// @lc code=end
