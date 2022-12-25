import java.util.Arrays;

/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        String[] words = s.split("[ ]+");
        System.out.println(Arrays.toString(words));
        return words[words.length - 1].length();
    }
}
// @lc code=end
