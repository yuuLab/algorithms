/*
 * @lc app=leetcode id=190 lang=java
 *
 * [190] Reverse Bits
 */

// @lc code=start
class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            // 末尾のbitを取得
            int lastBit = n & 1;
            // lastBit追加のため、1bit左シフトして空ける
            result <<= 1;
            result |= lastBit;
            // 次のために計算済みのbitを捨てる
            n >>>= 1;
        }
        return result;
    }
}
// @lc code=end
