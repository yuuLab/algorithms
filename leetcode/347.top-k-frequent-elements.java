import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode id=347 lang=java
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
class Solution {

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        // 同数の出現回数の数字を記録するためにリストの配列を作成
        List<Integer>[] bucket = new List[nums.length + 1];

        for (int key : map.keySet()) {
            int frequency = map.get(key);
            if (bucket[frequency] == null) {
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(key);
        }

        List<Integer> result = new ArrayList<Integer>();
        for (int pos = bucket.length - 1; pos >= 0 && result.size() < k; pos--) {
            if (bucket[pos] != null) {
                result.addAll(bucket[pos]);
            }
        }
        return toIntArray(result);
    }

    public int[] toIntArray(List<Integer> result) {
        int[] array = new int[result.size()];
        for (int i = 0; i < array.length; i++) {
            array[i] = Integer.valueOf(result.get(i));
        }
        return array;
    }

}
// @lc code=end
