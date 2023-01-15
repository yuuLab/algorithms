import java.util.HashSet;
import java.util.Set;

/*
 * @lc app=leetcode id=202 lang=java
 *
 * [202] Happy Number
 */

// @lc code=start
class Solution {
    public boolean isHappy(int n) {
        return isHappy(n, new HashSet<Integer>());
    }

    public boolean isHappy(int n, Set<Integer> doneSet) {
        int num = 0;
        while (n > 0) {
            int remain = n % 10;
            num += Math.pow(remain, 2);
            n /= 10;
        }
        if (num == 1)
            return true;

        if (doneSet.contains(num))
            return false;

        doneSet.add(num);
        return isHappy(num, doneSet);
    }
}
// @lc code=end
