import java.util.Stack;

/*
 * @lc app=leetcode id=101 lang=java
 *
 * [101] Symmetric Tree
 */

// @lc code=start
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;

        return this.isSymmetric(root.left, root.right);
    }

    private boolean isSymmetric(TreeNode leftNode, TreeNode rightNode) {
        if (leftNode == null && rightNode == null)
            return true;
        if (leftNode == null || rightNode == null)
            return false;

        if (leftNode.val == rightNode.val) {
            boolean isSameOutside = isSymmetric(leftNode.left, rightNode.right);
            boolean isSameInside = isSymmetric(leftNode.right, rightNode.left);
            return isSameInside && isSameOutside;
        }
        return false;
    }
}

class Solution2 {
    public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root.left);
        stack.push(root.right);
        while (!stack.empty()) {
            TreeNode n1 = stack.pop(), n2 = stack.pop();
            if (n1 == null && n2 == null)
                continue;
            if (n1 == null || n2 == null || n1.val != n2.val)
                return false;
            stack.push(n1.left);
            stack.push(n2.right);
            stack.push(n1.right);
            stack.push(n2.left);
        }
        return true;
    }
}
// @lc code=end
