N, M = map(int, input().split())
input_list = [n for n in range(1, N + 1)]
isused = [False] * N

def solution(step, in_list):
    if step == M:
        print(*in_list)
        return
    for i in range(N):
        if not isused[i]:
            isused[i] = True
            solution(step + 1, in_list + [input_list[i]])
            isused[i] = False

solution(0, [])