package algorithms.java.search;

public class BinarySearch {

  /**
   * Binary Search.
   * 
   * @param nums   a sorted array of distinct integers
   * @param target a target value
   * @return return the index if the target is found. If not, return the index
   *         where it would be if it were inserted in order
   */
  public int searchInsert(int[] nums, int target) {
    return searchInsert(nums, target, 0, nums.length - 1);
  }

  private int searchInsert(int[] nums, int target, int left, int right) {
    if (left > right) {
      // 見つからない場合、挿入すべきINDEXを返却
      int r = Math.max(0, right);
      return nums[r] < target ? r + 1 : r;
    }
    int mid = (left + right) / 2;
    if (nums[mid] == target) {
      return mid;
    }
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
    return searchInsert(nums, target, left, right);
  }
}
