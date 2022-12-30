package algorithms.java.basic;

public class MathUtil {

  /**
   * nの階乗を算出する。
   * 
   * @param n
   * @return nの階乗
   */
  public static int factorial(int n) {
    if (n == 0) {
      return 1;
    }
    int ret = factorial(n - 1);
    int ans = n * ret;
    return ans;
  }

  /**
   * Calculation Combination
   * 
   * @param n
   * @param r
   * @return nCr
   */
  public static int comb(int n, int r) {
    return factorial(n, r) / factorial(r);
  }

  private static int factorial(int n, int depth) {
    if (depth == 1) {
      return n;
    }
    int ret = factorial(n - 1, depth - 1);
    return n * ret;
  }

}
