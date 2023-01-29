/*
 * @lc app=leetcode id=33 lang=java
 *
 * [33] Search in Rotated Sorted Array
 */

// @lc code=start
class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 1) {
            return nums[0] == target ? 0 : -1;
        }
        // ソート済みの場合そのまま二分探索
        if (nums[0] < nums[nums.length - 1]) {
            return binarySearch(nums, target, 0, nums.length - 1);
        }
        int point = this.findRotatedPoint(nums);
        if (nums[point] == target) {
            return point;
        }
        if (nums[0] <= target && target <= nums[point - 1]) {
            return binarySearch(nums, target, 0, point);
        }
        return binarySearch(nums, target, point, nums.length - 1);
    }

    private int binarySearch(int[] nums, int target, int left, int right) {
        while (left <= right) {
            int middle = (left + right) / 2;
            if (nums[middle] == target)
                return middle;
            if (nums[middle] > target)
                right = middle - 1;
            if (nums[middle] < target)
                left = middle + 1;
        }
        return -1;
    }

    private int findRotatedPoint(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] > nums[mid + 1]) {
                return mid + 1;
            }
            if (nums[mid] < nums[mid - 1]) {
                return mid;
            }

            if (nums[mid] < nums[left]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
// @lc code=end
