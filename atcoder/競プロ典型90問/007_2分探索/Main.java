import java.util.*;

public class Main {
  public static void main(String[] args) {
    solve();
  }

  public static void solve() {
    Scanner sc = new Scanner(System.in);
    Integer N = Integer.parseInt(sc.next());
    sc.nextLine();
    long[] A = new long[N];
    String[] str = sc.nextLine().split(" ");
    for (int i = 0; i < N; i++) {
      A[i] = Long.parseLong(str[i]);
    }
    Arrays.sort(A);
    Integer Q = Integer.parseInt(sc.next());
    
    for (int i = 0; i < Q; i++) {
      long B = Long.parseLong(sc.next());
      System.out.println(Math.abs(binarySearch(A, B)-B));
    }
  }

  public static long binarySearch(long[] list, long target) {
    int left = 0;
    int right = list.length - 1;
    while (left <= right) {
      int mid = (left + right) / 2;
      if (list[mid] == target) {
        return target;
      }
      if (list[mid] > target) {
        right = mid - 1;
        continue;
      }
      left = mid + 1;
    }

    right = Math.max(0, right);
    left = Math.min(list.length-1, left);

    long rightVal = Math.abs(target - list[right]);
    long leftVal = Math.abs(target - list[left]);
    return rightVal < leftVal ? list[right] : list[left];
  }
}
