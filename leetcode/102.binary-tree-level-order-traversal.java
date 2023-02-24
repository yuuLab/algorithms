import java.util.ArrayDeque;
import java.util.Collections;
import java.util.Deque;
import java.util.List;
import java.util.Queue;

/*
 * @lc app=leetcode id=102 lang=java
 *
 * [102] Binary Tree Level Order Traversal
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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null)
            return Collections.emptyList();

        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        Deque<List<TreeNode>> q = new ArrayDeque<List<TreeNode>>();
        q.addLast(Arrays.asList(root));
        while (!q.isEmpty()) {
            List<TreeNode> nodes = q.removeFirst();

            List<Integer> values = new ArrayList<Integer>();
            List<TreeNode> sameLevels = new ArrayList<TreeNode>();

            for (TreeNode node : nodes) {
                values.add(node.val);

                if (node.left != null)
                    sameLevels.add(node.left);

                if (node.right != null)
                    sameLevels.add(node.right);
            }
            if (!sameLevels.isEmpty())
                q.addLast(sameLevels);

            if (!values.isEmpty())
                ans.add(values);
        }
        return ans;
    }

    public List<List<Integer>> levelOrder2(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null)
            return ans;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);

                if (node.left != null)
                    queue.add(node.left);

                if (node.right != null)
                    queue.add(node.right);

            }
            ans.add(level);
        }
        return ans;
    }
}
// @lc code=end
