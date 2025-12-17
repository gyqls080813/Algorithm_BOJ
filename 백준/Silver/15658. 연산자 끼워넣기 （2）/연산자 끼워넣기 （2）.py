N = int(input())
input_list = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈
ammount = list(map(int, input().split()))

max_number = -int(10e21)
min_number = int(10e21)

def solution(step, cum_num):
    global max_number, min_number
    if step == N:
        max_number = max(max_number, cum_num)
        min_number = min(min_number, cum_num)
        return
    
    # i번째 원소를 연산
    for i in range(4):
        if ammount[i] == 0:
            continue
        if i == 0:
            ammount[i] -= 1
            solution(step + 1 ,cum_num + input_list[step])
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
            else:
                next_cum = cum_num // input_list[step]
            solution(step + 1, next_cum)
            ammount[i] += 1

# 백트레킹 시작
start = 1
start_num = input_list[0]
solution(start, start_num)
print(f"{max_number}\n{min_number}")