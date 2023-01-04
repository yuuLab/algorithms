/*
 * @lc app=leetcode id=111 lang=java
 *
 * [111] Minimum Depth of Binary Tree
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
    public int minDepth(TreeNode root) {
        int minDepth = 0;
        if (root == null)
            return minDepth;

        return this.minDepth(root, minDepth + 1);
    }

    private int minDepth(TreeNode root, int depth) {

        // リーフノードの発見
        if (root.left == null && root.right == null)
            return depth;

        // 右ノードが続いているなら探索を続ける。
        if (root.left == null)
            return minDepth(root.right, depth + 1);
        // 左ノードが続いているなら探索を続ける。
        if (root.right == null)
            return minDepth(root.left, depth + 1);

        // 左右両方ノードが続いてるケース
        int left = minDepth(root.left, depth + 1);
        int right = minDepth(root.right, depth + 1);
        return Math.min(left, right);
    }
}

class Solution2 {
    public int minDepth(TreeNode root) {
        if (root == null)
            return 0;

        // Your are at lead node done call further just return
        if (root.left == null && root.right == null)
            return 1;

        int l = minDepth(root.left);
        int r = minDepth(root.right);

        // edge case
        if (root.left == null || root.right == null)
            return 1 + Math.max(l, r);

        return 1 + Math.min(l, r);
    }
}
// @lc code=end
