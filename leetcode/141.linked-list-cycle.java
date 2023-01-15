/*
 * @lc app=leetcode id=141 lang=java
 *
 * [141] Linked List Cycle
 */

// @lc code=start
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null)
            return false;

        ListNode node = head;
        while (node != null) {
            if (node.val == Integer.MAX_VALUE)
                return true;

            node.val = Integer.MAX_VALUE;
        }

        return false;
    }
}
// @lc code=end
