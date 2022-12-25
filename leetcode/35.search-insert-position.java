/*
 * @lc app=leetcode id=35 lang=java
 *
 * [35] Search Insert Position
 */

// @lc code=start
class Solution {
    public int searchInsert(int[] nums, int target) {
        return binarySearch(nums, target, 0, nums.length - 1);
    }

    public int binarySearch(int[] nums, int target, int left, int right) {
        if (left > right) {
            // 見つからない場合、挿入すべきINDEXを返却
            int r = Math.max(0, right);
            return nums[r] < target ? r + 1 : r;
        }
        int mid = (left + right) / 2;
        if (nums[mid] == target) {
            return mid;
        }
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
        return binarySearch(nums, target, left, right);
    }
}
// @lc code=end
