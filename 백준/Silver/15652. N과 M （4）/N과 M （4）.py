N, M = map(int, input().split())
input_list = [n for n in range(1, N + 1)]

def solution(step, in_list, now):
    if step == M:
        print(*in_list)
        return
    for i in range(now, N):
        solution(step + 1, in_list + [input_list[i]], i)

solution(0, [], 0)