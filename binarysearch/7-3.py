# 이진탐색 반복문으로 구현

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            array[mid] < target
            start = mid + 1

    return None

print(binary_search(array, 3, 0, len(array) - 1))