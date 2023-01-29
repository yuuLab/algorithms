/*
 * @lc app=leetcode id=153 lang=java
 *
 * [153] Find Minimum in Rotated Sorted Array
 */

// @lc code=start
class Solution {
    public int findMin(int[] nums) {
        if (nums.length == 1)
            return nums[0];

        int left = 0, right = nums.length - 1;
        // Alrady sorted array.
        if (nums[right] > nums[0]) {
            return nums[0];
        }

        while (left <= right) {
            int mid = (left + right) / 2;
            // min value
            if (nums[mid] > nums[mid + 1]) {
                return nums[mid + 1];
            }
            if (nums[mid] < nums[mid - 1]) {
                return nums[mid];
            }

            if (nums[mid] < nums[left]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return nums[left];
    }
}
// @lc code=end
