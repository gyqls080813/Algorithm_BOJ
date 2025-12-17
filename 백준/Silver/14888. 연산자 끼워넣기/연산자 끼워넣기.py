N = int(input())
input_list = list(map(int, input().split()))
ammount = list(map(int, input().split()))

max_num = -int(10e21)
min_num = int(10e21)

def solution(step, cum_num):
    global max_num, min_num
    if step == N:
        max_num = max(max_num, cum_num)
        min_num = min(min_num, cum_num)
    for i in range(4):
        if ammount[i] == 0:
            continue
        if i == 0:
            ammount[i] -= 1
            solution(step + 1, cum_num + input_list[step])
            ammount[i] += 1
        if i == 1:
            ammount[i] -= 1
            solution(step + 1, cum_num - input_list[step])
            ammount[i] += 1
        if i == 2:
            ammount[i] -= 1
            solution(step + 1, cum_num * input_list[step])
            ammount[i] += 1
        if i == 3:
            ammount[i] -= 1
            if cum_num < 0:
                next_cum = -(abs(cum_num) // input_list[step])
                solution(step + 1, next_cum)
            else:
                next_cum = cum_num // input_list[step]
                solution(step + 1, next_cum)
            ammount[i] += 1

start_step = 1
start_num = input_list[0]
solution(start_step, start_num)

print(f"{max_num}\n{min_num}")