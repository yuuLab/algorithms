/*
 * @lc app=leetcode id=704 lang=java
 *
 * [704] Binary Search
 */

// @lc code=start
class Solution {
    public int search(int[] nums, int target) {
        return binarySearch(nums, target, 0, nums.length - 1);

    }

    public int binarySearch(int[] nums, int target, int left, int right) {
        if (left > right)
            return -1;

        int middle = (left + right) / 2;
        if (nums[middle] == target)
            return middle;

        if (nums[middle] > target)
            return binarySearch(nums, target, left, middle - 1);

        return binarySearch(nums, target, middle + 1, right);
    }

    public int binarySearch2(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
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
}

// @lc code=end
