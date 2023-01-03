import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/*
 * @lc app=leetcode id=94 lang=java
 *
 * [94] Binary Tree Inorder Traversal
 */

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

// @lc code=start
class Solution {

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null) {
            return result;
        }
        this.inorderTraversal(root.left, result);
        result.add(root.val);
        this.inorderTraversal(root.right, result);
        return result;
    }

    private void inorderTraversal(TreeNode node, List<Integer> inordered) {
        if (node == null)
            return;

        if (node.left != null)
            this.inorderTraversal(node.left, inordered);
        // left node を走査完了後、自身の値を追加し、right node の走査へ
        inordered.add(node.val);
        if (node.right != null)
            this.inorderTraversal(node.right, inordered);
    }

    // stackを用いた解法
    public List<Integer> InorderTraversal2(TreeNode root) {
        List<Integer> list = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode node = root;
        while (node != null || stack.size() > 0) {
            if (node != null) {
                stack.push(node);
                node = node.left;
            } else {
                node = stack.pop();
                list.add(node.val);
                node = node.right;
            }
        }
        return list;
    }
}
// @lc code=end