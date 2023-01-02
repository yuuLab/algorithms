/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n == 0) {
            return;
        }

        int i = 0, j = 0, cnt = 0;
        int[] tmp = new int[n + m];
        while (i <= m - 1 || j <= n - 1) {
            if (i > m - 1) {
                tmp[cnt] = nums2[j++];
            } else if (j > n - 1) {
                tmp[cnt] = nums1[i++];
            } else {
                tmp[cnt] = nums1[i] <= nums2[j] ? nums1[i++] : nums2[j++];
            }
            cnt++;
        }
        for (int k = 0; k < nums1.length; k++) {
            nums1[k] = tmp[k];
        }
    }

    public void merge2(int[] nums1, int m, int[] nums2, int n) {
        int tail1 = m - 1, tail2 = n - 1, pos = m + n - 1;
        while (tail2 >= 0) {
            if (tail1 >= 0)
                nums1[pos--] = (nums1[tail1] > nums2[tail2]) ? nums1[tail1--] : nums2[tail2--];
            else
                nums1[pos--] = nums2[tail2--];
        }
    }
}
// @lc code=end
