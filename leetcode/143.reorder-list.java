/*
 * @lc app=leetcode id=143 lang=java
 *
 * [143] Reorder List
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
    public void reorderList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null)
            return;

        ListNode node = head;
        while (node.next.next != null) {
            ListNode endNode = this.getAndChangeEndNode(node);
            ListNode nextNode = node.next;
            endNode.next = nextNode;
            node.next = endNode;

            node = node.next.next;
        }
    }

    public ListNode getAndChangeEndNode(ListNode node) {
        if (node.next.next == null) {
            ListNode end = node.next;
            // 最後尾から2番目のNodeを最後尾にする。
            node.next = null;
            return end;
        }
        return getAndChangeEndNode(node.next);
    }
}

class Solution2 {
    public void reorderList(ListNode head) {
        if (head == null) {
            return;
        }

        // Find the middle node
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse the second half
        // Reverse the half after middle 1->2->3->4->5->6 to 1->2->3->6->5->4
        ListNode head2 = reverse(slow.next);
        slow.next = null;

        // Link the two halves together
        // Start reorder one by one 1->2->3->6->5->4 to 1->6->2->5->3->4
        while (head != null && head2 != null) {
            ListNode tmp1 = head.next;
            ListNode tmp2 = head2.next;
            head2.next = head.next;
            head.next = head2;
            head = tmp1;
            head2 = tmp2;
        }
    }

    private ListNode reverse(ListNode n) {
        ListNode prev = null;
        ListNode cur = n;
        while (cur != null) {
            ListNode tmp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = tmp;
        }
        return prev;
    }
}
// @lc code=end
