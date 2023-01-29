import java.util.Arrays;

/*
 * @lc app=leetcode id=74 lang=java
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int[] row = this.getTargetRow(matrix, target);
        System.out.println(Arrays.toString(row));
        return this.binarySearch(row, target) != -1;
    }

    public int[] getTargetRow(int[][] matrix, int target) {
        int idx = 0;
        for (int i = 1; i < matrix.length; i++) {
            if (target > matrix[i][0]) {
                idx = i - 1;
                break;
            }
        }
        return matrix[idx];
    }

    public int binarySearch(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int middle = (left + right) / 2;
            if (nums[middle] == target)
                return middle;
            if (nums[middle] > target)
                right = middle - 1;
            if (nums[middle] < target)
                left = middle + 1;
        }
        return -1;
    }
}

class Solution2 {
    public boolean searchMatrix(int[][] matrix, int target) {

        int row_num = matrix.length;
        int col_num = matrix[0].length;

        int begin = 0, end = row_num * col_num - 1;

        while (begin <= end) {
            int mid_row = (begin + end) / 2;
            int mid_value = matrix[mid_row / col_num][mid_row % col_num];

            if (mid_value == target) {
                return true;

            } else if (mid_value < target) {
                // Should move a bit further, otherwise dead loop.
                begin = mid_row + 1;
            } else {
                end = mid_row - 1;
            }
        }

        return false;
    }
}
// @lc code=end
