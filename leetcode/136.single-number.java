import java.util.Arrays;
import java.util.stream.IntStream;

/*
 * @lc app=leetcode id=136 lang=java
 *
 * [136] Single Number
 */

// @lc code=start
class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int cnt = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1] && cnt == 1)
                return nums[i - 1];

            if (nums[i] != nums[i - 1])
                cnt = 1;

            if (nums[i] == nums[i - 1])
                cnt++;
        }
        return -1;
    }
}

class Solution2 {
    public int singleNumber(int[] nums) {
        // 同じ数値同士のXORは0になることの性質を利用する。
        IntStream stream = Arrays.stream(nums);
        return stream.reduce((total, num) -> total ^ num).getAsInt();
    }
}
// @lc code=end
