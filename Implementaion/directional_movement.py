n = int(input())
plans = input().split()

# 여러개의 if문을 한 번의 if로 줄일 수 있음 # LRUD(왼쪽 오른쪽 위 아래)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

x, y = 1, 1

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x , y)