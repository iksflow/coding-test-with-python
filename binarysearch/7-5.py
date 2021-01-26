# 부품찾기 이진탐색 풀이
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))


def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return None
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


n_list.sort()
for i in range(m):
    if binary_search(n_list, m_list[i], 0, len(n_list) - 1):
        print("yes", end = " ")
    else:
        print("no", end=" ")
