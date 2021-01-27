# 떡볶이 떡 만들기

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
start = 0
end = array[-1]
result = 0
print("start", start)
print("end", end)
while start <= end:
    mid = (end + start) // 2
    sum = 0
    # 중간값보다 긴것들만 잘라본다
    for i in range(len(array)):
        if mid < array[i]:
           sum += array[i] - mid
    # 절단한 합계가 m값과 일치하다면 값을 저장하고 반복문을 탈출
    if sum == m:
        result = mid
        break
    # 합계가 모자르다면 더 잘라야하므로 절단기의 높이를 낮춰야한다. 즉 중간값을 아래방향으로 이동
    elif sum < m:
        end = mid
    # 합계가 넘친다면 덜 잘라야하므로 절단기의 높이를 높여야한다. 즉 중간값을 윗방향으로 이동
    else:
        start = mid


print(result)