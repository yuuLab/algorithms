import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=167 lang=java
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];
        // {key, value} = {remain, index}
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < numbers.length; i++) {
            int n = numbers[i];
            if (map.containsKey(n)) {
                result[0] = map.get(n);
                result[1] = i + 1;
                return result;
            }
            map.put(target - n, i + 1);
        }
        return result;
    }

    public int[] twoSum2(int[] numbers, int target) {
        int start = 0, end = numbers.length - 1;
        while (start < end) {
            if (numbers[start] + numbers[end] == target)
                break;
            if (numbers[start] + numbers[end] < target)
                start++;
            else
                end--;
        }
        return new int[] { start + 1, end + 1 };
    }
}
// @lc code=end
