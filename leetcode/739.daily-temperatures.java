import java.util.Stack;

/*
 * @lc app=leetcode id=739 lang=java
 *
 * [739] Daily Temperatures
 */

// @lc code=start
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        if (temperatures.length == 1) {
            return new int[] { 0 };
        }

        int[] answer = new int[temperatures.length];
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(0);
        int day = 1;
        while (stack.size() > 0 && day < temperatures.length) {
            if (temperatures[stack.peek()] < temperatures[day]) {
                int size = stack.size();
                for (int i = 0; i < size; i++) {
                    int idx = stack.pop();
                    int pre = temperatures[idx];
                    if (pre >= temperatures[day]) {
                        stack.push(idx);
                        break;
                    }
                    answer[idx] = day - idx;
                }
            }
            stack.push(day);
            day++;
        }
        return answer;
    }
}

class Solution2 {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] ret = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int idx = stack.pop();
                ret[idx] = i - idx;
            }
            stack.push(i);
        }
        return ret;
    }
}
// @lc code=end
