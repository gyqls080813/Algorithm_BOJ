N = int(input())
input_list = list(input().split() for _ in range(N))

teacher = []

for i in range(N):
    for j in range(N):
        if input_list[i][j] == "T":
            teacher.append([i, j])

can_put = []
for teacher_x, teacher_y in teacher:
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = teacher_x, teacher_y
        while nx + dx < N and ny + dy < N and nx + dx >= 0 and ny + dy >= 0:
            nx += dx
            ny += dy
            if input_list[nx][ny] == "S":
                break
            if [nx, ny] in can_put:
                continue
            can_put.append([nx, ny])

is_can_put = [False] * len(can_put)

def check_true():
    is_true = True
    for teacher_x, teacher_y in teacher:
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = teacher_x, teacher_y
            while nx + dx < N and ny + dy < N and nx + dx >= 0 and ny + dy >= 0:
                nx += dx
                ny += dy
                if input_list[nx][ny] == "B":
                    break
                if input_list[nx][ny] == "S":
                    is_true = False
                    break
            if not is_true:
                break
        if not is_true:
            break
    return is_true

result = 'NO'

def solution(step):
    global result
    if step == 3:
        local_result = check_true()
        if local_result:
            result = "YES"
        return
    
    for i in range(len(can_put)):
        if not is_can_put[i]:
            is_can_put[i] = True
            input_list[can_put[i][0]][can_put[i][1]] = 'B'
            solution(step+1)
            is_can_put[i] = False
            input_list[can_put[i][0]][can_put[i][1]] = 'X'

solution(0)
print(result)        