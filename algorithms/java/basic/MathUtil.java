package algorithms.java.basic;

public class MathUtil {

  /**
   * nの階乗を算出する。
   * 
   * @param n
   * @return nの階乗
   */
  public int factorial(int n) {
    if (n == 0) {
      return 1;
    }
    int ret = factorial(n - 1);
    int ans = n * ret;
    return ans;
  }
}
