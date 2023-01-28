import java.util.Arrays;

/*
 * @lc app=leetcode id=853 lang=java
 *
 * [853] Car Fleet
 */

// @lc code=start
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        if (n < 2)
            return n;

        double[][] cars = new double[n][2];
        for (int i = 0; i < n; i++) {
            double arriveTime = ((double) target - (double) position[i]) / (double) speed[i];
            cars[i][0] = position[i];
            cars[i][1] = arriveTime;
        }
        Arrays.sort(cars, (a, b) -> (int) a[0] - (int) b[0]);
        int ans = 0;
        for (int i = n - 1; i > 0; i--) {
            if (cars[i][1] < cars[i - 1][1]) {
                // 一つ前の車の方が時間がかかっている場合、合流できないので集団は分かれる。
                ans++;
            } else {
                // スタート位置が小さいにも関わらず早く到着しているので合流する。
                // 一つの集団とし、遅い方の到着時間に合わせる。
                cars[i - 1][1] = cars[i][1];
            }
        }
        return ans + 1;
    }
}

// @lc code=end