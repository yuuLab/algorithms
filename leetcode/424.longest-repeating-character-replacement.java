/*
 * @lc app=leetcode id=424 lang=java
 *
 * [424] Longest Repeating Character Replacement
 */

// @lc code=start
class Solution {

    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int start = 0, maxCount = 0, maxLength = 0;
        for (int end = 0; end < s.length(); end++) {
            maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
            // end-start+1-maxCount -> そのウィンドウ内で最も多く出現する文字ではない文字の数にちょうど等しい。
            // ex："xxxyz" : end-start+1-maxCount = 2 (yz)
            // これがkより大きくなるとwindowに収まっていないのでstart位置をくり上げる。
            while (end - start + 1 - maxCount > k) {
                count[s.charAt(start) - 'A']--;
                start++;
            }
            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
}
// @lc code=end
