import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution {

    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> result = new ArrayList<>();
        Set<String> done = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            Map<Integer, Integer> map = new HashMap<>();
            int target = 0 - nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                int n = nums[j];
                if (map.containsKey(n)) {
                    int[] ans = { nums[i], map.get(n), nums[j] };
                    Arrays.sort(ans);
                    String key = Arrays.toString(ans);
                    if (done.contains(key))
                        continue;

                    List<Integer> list = Arrays.asList(nums[i], map.get(n), nums[j]);
                    result.add(list);
                    done.add(key);
                }
                int re = target - nums[j];
                map.put(re, n);
            }
        }
        return result;
    }

    public List<List<Integer>> threeSum2(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();
        if (nums.length == 0)
            return Collections.emptyList();

        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0)
                    res.add(Arrays.asList(nums[i], nums[j++], nums[k--]));
                else if (sum > 0)
                    k--;
                else if (sum < 0)
                    j++;
            }

        }
        return new ArrayList<>(res);
    }
}
// @lc code=end
