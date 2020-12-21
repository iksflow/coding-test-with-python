# 특정 수를 총 M번 더했을 때 얻을 수 있는 최대값. 단, 연속해서 같은 수를 더할 수 있는 최대 회수는 K번.
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
print(n, m, k)
print(data)
first = data[n - 1]
second = data[n - 2]
print(first)
print(second)

result = 0


# # 첫번째 방법 - 직접 더하는 과정 O(N)
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

# 두번째 방법 - 분석한 패턴을 통해 계산 O(1)
cycle = m // (k + 1)
remain = m % (k + 1)
result = (first * k + second) * cycle + (remain * first)
print(cycle)
print(result)