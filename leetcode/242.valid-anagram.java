import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=242 lang=java
 *
 * [242] Valid Anagram
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if (map.containsKey(c)) {
                Integer val = map.get(c) - 1;
                if (val == 0)
                    map.remove(c);
                else
                    map.put(c, val);
            } else {
                return false;
            }
        }
        return true;
    }

    public boolean isAnagram2(String s, String t) {
        int[] alphabets = new int[26];
        for (int i = 0; i < s.length(); i++) {
            alphabets[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            alphabets[t.charAt(i) - 'a']--;
        }

        for (int cnt : alphabets) {
            if (cnt != 0)
                return false;
        }
        return true;
    }
}
// @lc code=end
