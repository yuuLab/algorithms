import java.util.Stack;

/*
 * @lc app=leetcode id=150 lang=java
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
class Solution {
    public int evalRPN(String[] tokens) {
        if (tokens.length == 1)
            return Integer.valueOf(tokens[0]);

        int result = 0;
        Stack<String> stack = new Stack<String>();
        for (String token : tokens) {
            if (isOperator(token)) {
                int a = Integer.parseInt(stack.pop());
                int b = Integer.parseInt(stack.pop());
                int culc = 0;
                if ("+".equals(token))
                    culc += b + a;
                if ("-".equals(token))
                    culc += b - a;
                if ("*".equals(token))
                    culc += b * a;
                if ("/".equals(token))
                    culc += b / a;
                result += culc;
                stack.push(String.valueOf(culc));
                continue;
            }
            stack.push(token);
        }
        return result;
    }

    private boolean isOperator(String token) {
        return "+".equals(token)
                || "-".equals(token)
                || "*".equals(token)
                || "/".equals(token);
    }

}
// @lc code=end
