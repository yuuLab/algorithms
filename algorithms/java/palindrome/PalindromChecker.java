package algorithms.java.palindrome;

import java.util.Objects;

public class PalindromChecker {

  /**
   * 回文判定。
   * 
   * @param x 解析対象数値
   * @return 回文であればtrue, それ以外false
   */
  public static boolean isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
      return false;
    }
    int reverse = 0;
    while (x > reverse) {
      reverse = reverse * 10 + x % 10;
      x /= 10;
    }
    return x == reverse || x == reverse / 10;
  }

  /**
   * 回文判定。
   * 
   * @param x 解析対象数値
   * @return 回文であればtrue, それ以外false
   */
  public static boolean isPalindrome(String x) {
    String reverse = new StringBuffer(x).reverse().toString();
    return Objects.equals(reverse, x);
  }

}
