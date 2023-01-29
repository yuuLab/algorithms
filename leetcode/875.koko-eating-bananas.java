
/*
 * @lc app=leetcode id=875 lang=java
 *
 * [875] Koko Eating Bananas
 */

// @lc code=start
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1, high = this.getMaxPile(piles);

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canEatPiles(piles, mid, h)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    boolean canEatPiles(int[] piles, int speed, int hours) {
        long timeTaken = 0;
        for (int i = 0; i < piles.length; i++) {
            timeTaken += (piles[i] / speed);
            if (piles[i] % speed != 0)
                timeTaken++;
        }
        return timeTaken <= hours;
    }

    private int getMaxPile(int[] piles) {
        int maxPile = Integer.MIN_VALUE;
        for (int pile : piles) {
            maxPile = Math.max(pile, maxPile);
        }
        return maxPile;
    }
}
// @lc code=end
