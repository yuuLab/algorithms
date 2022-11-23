def binary_search_strict(numbers: list, value: int) -> int:
    """
    二分探索:一致する値のインデントを返却する。見つからない場合は-1を返却する。
    """
    def _binary_search(numbers: list, value: int,
                       left: int, right: int) -> int:
        if left > right:
            return -1

        middle = (left + right) // 2
        if numbers[middle] == value:
            return middle
        elif numbers[middle] < value:
            return _binary_search(numbers, value, middle + 1, right)
        else:
            return _binary_search(numbers, value, left, middle - 1)

    return _binary_search(numbers, value, 0, len(numbers) - 1)


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
