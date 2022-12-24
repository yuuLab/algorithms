import java.util.Arrays;

/*
 * @lc app=leetcode id=26 lang=java
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        for (int n : nums) {
            if (k == 0 || n > nums[k - 1]) {
                nums[k++] = n;
            }
        }
        System.out.println(Arrays.toString(nums));
        return k;
    }
}
// @lc code=end
