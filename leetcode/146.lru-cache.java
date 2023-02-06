import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=146 lang=java
 *
 * [146] LRU Cache
 */

// @lc code=start
class LRUCache {

    private Map<Integer, ListNode> cache;

    private DoubleLinkedList dlinkedList;

    private Integer capacity;

    public LRUCache(int capacity) {
        this.cache = new HashMap<>();
        this.dlinkedList = new DoubleLinkedList();
        this.capacity = capacity;
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            ListNode node = cache.get(key);
            this.dlinkedList.moveToHead(node);
            return node.value;
        }
        return -1;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            ListNode node = cache.get(key);
            node.value = value;
            this.cache.put(key, node);
            this.dlinkedList.moveToHead(node);
        } else {
            if (this.cache.size() >= this.capacity) {
                ListNode node = this.dlinkedList.popTail();
                this.cache.remove(node.key);
            }
            ListNode node = new ListNode(key, value);
            this.cache.put(key, node);
            this.dlinkedList.addNode(node);
        }
    }
}

class DoubleLinkedList {
    ListNode head;
    ListNode tail;
    Integer length;

    DoubleLinkedList() {
        this.head = new ListNode(0, 0); // dummy
        this.tail = new ListNode(0, 0); // dummy
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.length = 0;
    }

    public void addNode(ListNode node) {
        node.prev = this.head;
        node.next = this.head.next;
        this.head.next = node;
        node.next.prev = node;
        this.length++;
    }

    public void removeNode(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        this.length--;
    }

    public void moveToHead(ListNode node) {
        this.removeNode(node);
        this.addNode(node);
    }

    // pop the current tail.
    public ListNode popTail() {
        ListNode res = tail.prev;
        this.removeNode(res);
        return res;
    }

}

class ListNode {
    int key;
    int value;
    ListNode next;
    ListNode prev;

    ListNode(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end
