N, M = map(int, input().split())
input_list = [list(map(int, input())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

start_x = 0
start_y = 0

queue_x = []
queue_y = []

queue_x.append(start_x)
queue_y.append(start_y)
dist[start_x][start_y] = 1

change = False
while queue_x and queue_y:
    cur_x = queue_x.pop(0)
    cur_y = queue_y.pop(0)

    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if input_list[nx][ny] == 0 or dist[nx][ny] != 0:
            continue

        if nx == N - 1 and ny == M - 1:
            print(dist[cur_x][cur_y] + 1)
            change = True
            break

        queue_x.append(nx)
        queue_y.append(ny)
        dist[nx][ny] = dist[cur_x][cur_y] + 1

    if change:
        break