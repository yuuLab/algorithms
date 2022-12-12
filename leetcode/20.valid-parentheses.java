package leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Stack;

/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {

    public boolean isValid(String s) {
        Deque<String> deque = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            String str = String.valueOf(s.charAt(i));
            if (str.equals("(")) {
                deque.push(")");
            } else if (str.equals("{")) {
                deque.push("}");
            } else if (str.equals("[")) {
                deque.push("]");
            } else {
                if (deque.isEmpty()) {
                    return false;
                }
                if (!deque.pop().equals(str)) {
                    return false;
                }
            }
        }
        return deque.isEmpty();
    }

    public boolean isValid2(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }
        return stack.isEmpty();
    }
}
// @lc code=end