import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=169 lang=java
 *
 * [169] Majority Element
 */

// @lc code=start
class Solution {
    public int majorityElement(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        Map<Integer, Integer> numsMap = new HashMap<Integer, Integer>();
        int majority = nums.length / 2;
        int ans = 0;
        for (int n : nums) {
            if (numsMap.containsKey(n)) {
                int cnt = numsMap.get(n) + 1;
                if (cnt > majority) {
                    ans = n;
                    break;
                }
                numsMap.put(n, cnt);
            } else {
                numsMap.put(n, 1);
            }
        }
        return ans;
    }
}

class Solution2 {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}
// @lc code=end
