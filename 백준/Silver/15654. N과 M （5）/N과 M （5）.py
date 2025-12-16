N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
isused = [False] * N

def solution(step, in_list):
    if step == M:
        print(*in_list)
        return 0
    for i in range(N):
        if not isused[i]:
            isused[i] = True
            solution(step + 1, in_list + [input_list[i]])
            isused[i] = False

solution(0, [])