import java.util.HashSet;
import java.util.Set;

/*
 * @lc app=leetcode id=36 lang=java
 *
 * [36] Valid Sudoku
 */

// @lc code=start
class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            Set<Character> rows = new HashSet<Character>();
            Set<Character> cols = new HashSet<Character>();
            Set<Character> cube = new HashSet<Character>();
            for (int j = 0; j < 9; j++) {
                // 横検証
                if (board[i][j] != '.' && !rows.add(board[i][j]))
                    return false;
                // 縦検証
                if (board[j][i] != '.' && !cols.add(board[j][i]))
                    return false;
                // 3×3検証
                int rowIndex = 3 * (i / 3) + (j / 3);
                int colIndex = j % 3 + 3 * (i % 3);
                if (board[rowIndex][colIndex] != '.' && !cube.add(board[rowIndex][colIndex]))
                    return false;
            }
        }
        return true;
    }
}
// @lc code=end
