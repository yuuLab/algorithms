import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

/*
 * @lc app=leetcode id=981 lang=java
 *
 * [981] Time Based Key-Value Store
 */

// @lc code=start
class TimeMap {

    // TreeMapで昇順に並んだ{timestamp : value}を格納する。
    Map<String, TreeMap<Integer, String>> keyTimeMap;

    public TimeMap() {
        this.keyTimeMap = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        if (!this.keyTimeMap.containsKey(key)) {
            this.keyTimeMap.put(key, new TreeMap<>());
        }
        this.keyTimeMap.get(key).put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        if (!this.keyTimeMap.containsKey(key)) {
            return "";
        }
        if (this.keyTimeMap.get(key).containsKey(timestamp)) {
            return this.keyTimeMap.get(key).get(timestamp);
        }
        Map.Entry<Integer, String> val = this.keyTimeMap.get(key).lowerEntry(timestamp);
        return val == null ? "" : val.getValue();
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
// @lc code=end
