N = int(input())
A = list(map(int, input().split()))

Q = int(input())

def binary_search(numbers: list, value:int) -> int:
    """
    二分探索:一致する値のインデントを返却する。見つからない場合は、絶対値が一番小さい値のインデックスを返却する。
    """
    left, right = 0, len(numbers)-1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    idx1 = min(left, len(numbers)-1)
    idx2 = max(right, 0)
    l = abs(numbers[idx1] - value)
    r = abs(numbers[idx2] - value)
    return idx1 if l < r else idx2

A.sort()
for i in range(Q):
    B = int(input())
    idx = binary_search(A, B)
    print(abs(B-A[idx]))