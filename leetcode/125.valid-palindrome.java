import java.util.Objects;

/*
 * @lc app=leetcode id=125 lang=java
 *
 * [125] Valid Palindrome
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        if (s == null) {
            return true;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            String a = String.valueOf(s.charAt(i)).toLowerCase();
            if (a.matches("[a-z]")) {
                sb.append(a);
            }
        }
        String formatted = sb.toString();
        String reverse = new StringBuffer(formatted).reverse().toString();
        return Objects.equals(reverse, formatted);
    }
}

class Solution2 {
    public boolean isPalindrome(String s) {
        String tmp = s.replace("[^a-zA-Z0-9]", "").toLowerCase();
        String reverse = new StringBuffer(tmp).reverse().toString();
        return Objects.equals(reverse, tmp);
    }
}
// @lc code=end
