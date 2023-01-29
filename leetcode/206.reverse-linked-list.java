/*
 * @lc app=leetcode id=206 lang=java
 *
 * [206] Reverse Linked List
 */

// @lc code=start
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null)
            return null;
        if (head.next == null)
            return head;

        return this.reverseList(head.next, new ListNode(head.val));
    }

    public ListNode reverseList(ListNode node, ListNode preNode) {
        if (node.next == null) {
            return new ListNode(node.val, preNode);
        }
        ListNode n = node.next;
        node.next = preNode;
        return reverseList(n, node);
    }

    public ListNode reverseList2(ListNode head) {
        /* iterative solution */
        ListNode newHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }
}
// @lc code=end
