/*
 * @lc app=leetcode id=238 lang=java
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
class Solution {
    public int[] productExceptSelf(int[] nums) {

        Integer product = 1;
        int zeroCnt = 0;
        for (int n : nums) {
            if (n == 0) {
                zeroCnt += 1;
                continue;
            }
            product = product * n;
        }
        int[] answer = new int[nums.length];
        if (zeroCnt > 1) {
            return answer;
        }
        if (zeroCnt == 1) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == 0) {
                    answer[i] = product;
                    break;
                }
            }
            return answer;
        }
        for (int i = 0; i < nums.length; i++) {
            answer[i] = product / nums[i];
        }
        return answer;
    }

    public int[] productExceptSelf2(int[] nums) {
        // nums = [1, 2, 3, 4]
        int n = nums.length;
        int[] answer = new int[n];
        answer[0] = 1;
        // answer = [1, 1, 2, 6]
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        int right = 1;
        // answer = [1, 2, 8, 6]
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= right;
            right *= nums[i];
        }
        return answer;
    }
}
// @lc code=end
