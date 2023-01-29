/*
 * @lc app=leetcode id=19 lang=java
 *
 * [19] Remove Nth Node From End of List
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null || head.next == null)
            return null;

        int cnt = this.remove(head, n);
        // 先頭を削除するケース
        if (cnt == n) {
            return head.next;
        }
        return head;
    }

    private int remove(ListNode node, int n) {
        if (node.next == null) {
            return 1;
        }

        int cnt = remove(node.next, n);
        if (cnt == -1) {
            return -1;
        }

        if (cnt == n) {
            node.next = node.next.next;
            return -1;
        }
        return cnt + 1;
    }
}

class Solution2 {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode start = new ListNode(0);
        start.next = head;
        ListNode slow = start, fast = start;

        // fastとslowでn+1の間隔を作り、同じ速度で移動させる。
        // fastが終点に達した場とき、slowはn+1の後ろのNodeにいるので、次のNodeをスキップすれば良い。
        for (int i = 1; i <= n + 1; i++) {
            fast = fast.next;
        }
        // Move fast to the end, maintaining the gap
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        // Skip the desired node
        slow.next = slow.next.next;
        return start.next;
    }
}
// @lc code=end
