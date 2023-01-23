import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode id=49 lang=java
 *
 * [49] Group Anagrams
 */

// @lc code=start
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null)
            return new ArrayList<>();

        Map<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] c = strs[i].toCharArray();
            Arrays.sort(c);
            String val = String.valueOf(c);
            if (map.containsKey(val)) {
                map.get(val).add(strs[i]);
            } else {
                List<String> l = new ArrayList<>();
                l.add(strs[i]);
                map.put(val, l);
            }
        }
        List<List<String>> result = new ArrayList<>();
        map.forEach((key, value) -> result.add(value));
        return result;
    }
}
// @lc code=end
