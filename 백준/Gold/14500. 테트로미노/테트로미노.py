N, M = map(int, input().split())
input_list = [list(map(int, input().split())) for _ in range(N)]
isgo = [[False] * M for _ in range(N)]
max_result = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(step, cum_num, dir):
    global max_result
    if step == 4:
        max_result = max(max_result, cum_num)
        return
    # 이전 위치 x, y
    for direct in range(4):
        x, y = dir[0], dir[1]
        # 현재 위치 dir_x, dir_y
        dir_x = x + dx[direct]
        dir_y = y + dy[direct]
        if dir_x < 0 or dir_y < 0 or dir_x >= N or dir_y >= M:
            continue
        if isgo[dir_x][dir_y]:
            continue
        isgo[dir_x][dir_y] = True
        if step == 2:
            solution(step + 1, cum_num + input_list[dir_x][dir_y], [x, y])
        solution(step + 1, cum_num + input_list[dir_x][dir_y], [dir_x, dir_y])
        isgo[dir_x][dir_y] = False

for i in range(N):
    for j in range(M):
        isgo[i][j] = True
        solution(1, input_list[i][j], [i, j])
        isgo[i][j] = False

print(max_result)