N, S = map(int, input().split())
input_list = list(map(int, input().split()))
result = 0

def solution(idx, cum_sum):
    global result
    if idx == N:
        if cum_sum == S:
            result += 1
        return
    solution(idx + 1, cum_sum + input_list[idx])
    solution(idx + 1, cum_sum)

solution(0, 0)
if S == 0:
    result -= 1
print(result)
