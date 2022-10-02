def binary_search(numbers: list, value:int) -> int:
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
    if numbers[idx1] >= value :
        return idx1
    if numbers[idx2] >= value:
        return idx2
    
    return -1

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
for i in range(Q):
    value = int(input())
    idx = binary_search(A, value)
    if idx == -1:
        print(0)
    else:
        print(N-idx)