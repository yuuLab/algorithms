import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=128 lang=java
 *
 * [128] Longest Consecutive Sequence
 */

// @lc code=start
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0)
            return 0;

        Arrays.sort(nums);
        int longest = 1;
        int expectedNext = nums[0] + 1;
        int current = 1;
        for (int i = 1; i < nums.length; i++) {
            int n = nums[i];
            if (n == expectedNext - 1) {
                continue;
            }
            if (n == expectedNext) {
                current += 1;
            }
            if (n != expectedNext) {
                current = 1;
            }
            longest = Math.max(longest, current);
            expectedNext = n + 1;
        }
        return longest;
    }

    public int longestConsecutive2(int[] num) {
        int res = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int n : num) {
            if (!map.containsKey(n)) {
                int left = (map.containsKey(n - 1)) ? map.get(n - 1) : 0;
                int right = (map.containsKey(n + 1)) ? map.get(n + 1) : 0;
                // sum: length of the sequence n is in
                int sum = left + right + 1;
                map.put(n, sum);

                // keep track of the max length
                res = Math.max(res, sum);

                // extend the length to the boundary(s)
                // of the sequence
                // will do nothing if n has no neighbors
                map.put(n - left, sum);
                map.put(n + right, sum);
            } else {
                // duplicates
                continue;
            }
        }
        return res;
    }
}
// @lc code=end
