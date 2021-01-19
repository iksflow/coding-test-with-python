# 게임 개발

# 맵 크기 설정
n, m = map(int, input().split())

# 방문 위치 기억
d = [[0] * m for _ in range(n)]

# 캐릭터 위치, 방향 설정
x, y, direction = map(int, input().split())

# 시작 위치 카운트
d[x][y] = 1

# 게임 맵 생성
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 이동방향 설정
# 0=북, 1=동, 2=남, 3=서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 육지인 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 뒤로 가는 좌표
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있는 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)