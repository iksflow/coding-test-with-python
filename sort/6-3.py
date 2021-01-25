# 퀵 정렬 호어 알고리즘

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    print("left")
    while left <= right:
        while array[pivot] >= array[left] and left <= end:
            left += 1
        while array[right] >= array[pivot] and right > start:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)




quick_sort(array, 0, len(array)- 1)
print(array)

