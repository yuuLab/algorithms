/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        String s1 = this.getReversedString(l1);
        String s2 = this.getReversedString(l2);
        String sum = this.sum(s1, s2);
        return this.convert(sum, sum.length() - 1);
    }

    public String sum(String s1, String s2) {

        int l1 = s1.length() - 1;
        int l2 = s2.length() - 1;
        StringBuilder sb = new StringBuilder();
        int tmp = 0;
        while (l1 >= 0 || l2 >= 0) {
            int i1 = l1 >= 0 ? Integer.valueOf(String.valueOf(s1.charAt(l1))) : 0;
            int i2 = l2 >= 0 ? Integer.valueOf(String.valueOf(s2.charAt(l2))) : 0;
            int sum = i1 + i2 + tmp;
            sb.append(String.valueOf((sum % 10)));
            tmp = sum / 10;
            l1--;
            l2--;
        }
        if (tmp > 0)
            sb.append(String.valueOf(tmp));
        return sb.reverse().toString();
    }

    public String getReversedString(ListNode node) {
        if (node.next == null) {
            return String.valueOf(node.val);
        }

        StringBuilder sb = new StringBuilder();
        sb.append(this.getReversedString(node.next));
        sb.append(String.valueOf(node.val));
        return sb.toString();
    }

    public ListNode convert(String value, int idx) {
        if (idx == 0) {
            int val = Integer.valueOf(String.valueOf(value.charAt(idx)));
            return new ListNode(val);
        }

        int val = Integer.valueOf(String.valueOf(value.charAt(idx)));
        ListNode start = new ListNode(val);
        start.next = convert(value, idx - 1);
        return start;
    }
}

class Solution2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0); // creating an dummy list
        ListNode curr = dummy; // intialising an pointer
        int carry = 0; // intialising our carry with 0 intiall
        // while loop will run, until l1 OR l2 not reaches null OR if they both reaches
        // null. But our carry has some value in it.
        // We will add that as well into our list
        while (l1 != null || l2 != null || carry == 1) {
            int sum = 0; // intialising our sum
            if (l1 != null) { // adding l1 to our sum & moving l1
                sum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) { // adding l2 to our sum & moving l2
                sum += l2.val;
                l2 = l2.next;
            }
            sum += carry; // if we have carry then add it into our sum
            carry = sum / 10; // if we get carry, then divide it by 10 to get the carry
            ListNode node = new ListNode(sum % 10); // the value we'll get by moduloing it, will become as new node so.
                                                    // add it to our list
            curr.next = node; // curr will point to that new node if we get
            curr = curr.next; // update the current every time
        }
        return dummy.next; // return dummy.next bcz, we don't want the value we have consider in it
                           // intially!!
    }
}
// @lc code=end
