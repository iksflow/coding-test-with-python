# 이진 탐색 재귀함수로 구현
# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
array = [1, 2, 3, 4, 5]


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


print(binary_search(array, 4, 0, len(array) - 1))