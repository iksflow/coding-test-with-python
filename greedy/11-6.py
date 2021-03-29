# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    result = -1
    index = 0
    if sum(food_times) == 0 or sum(food_times) <= k:
        return result

    while 0 < k:
        if 0 < food_times[index]:
            food_times[index] -= 1
            k -= 1
        index = (index + 1) % len(food_times)

    return index + 1

ans = solution([3, 1, 2], 4);

print('answer =', ans)