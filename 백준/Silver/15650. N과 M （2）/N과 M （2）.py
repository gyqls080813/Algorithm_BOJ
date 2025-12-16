N, M = map(int, input().split())
input_list = [n for n in range(1, N + 1)]
isused = [False] * N

def solution(step, in_list, now):
    if step == M:
        print(*in_list)
    for i in range(now, N):
        if not isused[i]:
            isused[i] = True
            solution(step + 1, in_list + [input_list[i]], i)
            isused[i] = False

solution(0, [], 0)

