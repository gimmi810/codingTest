'''
Q. 상하좌우
    N * N 크기의 정사각형 공간을 계획서대로 이동하여 최종 도착 좌표 구하기

    조건 >>
    L: 왼쪽으로 한 칸 이동
    R: 오른쪽으로 한 칸 이동
    U: 위로 한 칸 이동
    D: 아래로 한 칸 이동
    시작 : (1,1)

    5
    R R R U D D

    원리 >>
    구현문제
    연산횟수는 이동횟수에 비례
'''

n = int(input('공간 사이즈 입력: '))
plan_list = list(map(str, input('계획서 :').split()))

x, y = 1, 1
cmd_x = {'U':0, 'D':0, 'R':1, 'L':-1}
cmd_y = {'U':-1, 'D':1, 'R':0, 'L':0}

for plan in plan_list:
    tmp_x = x + cmd_x[plan]
    if tmp_x > 0 and tmp_x <= n:
        x = tmp_x

    tmp_y = y + cmd_y[plan]
    if tmp_y > 0 and tmp_y <= n:
        y = tmp_y

print(str(y)+' '+str(x))



# 답안 예시 >>
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)