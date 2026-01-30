from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
input_list = [[] for _ in range(n)]

for i in range(n):
    column = list(map(int, input().split()))
    input_list[i] = column

is_go = [[False] * m for _ in range(n)]

max_size = 0
picture = 0

def dfs(start_x, start_y):
    count = 1
    q = deque()
    q.append((start_x, start_y))
    is_go[start_x][start_y] = True
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if is_go[nx][ny] or input_list[nx][ny] != 1:
                continue
            q.append((nx, ny))
            is_go[nx][ny] = True
            count += 1
    return count

for i in range(n):
    for j in range(m):
        if input_list[i][j] == 1 and not is_go[i][j]:
            size = dfs(i, j)
            picture += 1
            max_size = max(max_size, size)

print(picture)
print(max_size)