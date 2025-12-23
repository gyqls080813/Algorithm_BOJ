N = int(input())
input_numbers = list(map(int, input().split()))
amounts = list(map(int, input().split()))
# [수정] % 대신 /로 통일
oper_symbols = ['+', '-', '*', '/']

max_num = -float('inf')
min_num = float('inf')

def calculater(combined_list):
    result_list = []
    operator_stack = []
    prim = {
        '+': 1, '-': 1,
        '*': 2, '/': 2,
    }
    
    # 1. 후위 표기법 변환
    for i in combined_list:
        if i in prim:  # 연산자인 경우
            while operator_stack and prim[operator_stack[-1]] >= prim[i]:
                result_list.append(operator_stack.pop())
            operator_stack.append(i)
        else:  # 숫자인 경우
            result_list.append(i)
            
    while operator_stack:
        result_list.append(operator_stack.pop())

    # 2. 후위 표기법 연산
    stack = []
    for now in result_list:
        if now in prim:
            second = stack.pop()
            first = stack.pop()
            if now == '+':
                stack.append(first + second)
            elif now == '-':
                stack.append(first - second)
            elif now == '*':
                stack.append(first * second)
            elif now == '/':
                # C++14 기준 나눗셈: 0쪽으로 절사 (int(a/b))
                if first < 0:
                    stack.append(-(-first // second))
                else:
                    stack.append(first // second)
        else:
            stack.append(now)
    return stack[0]

def solution(step, cul_list):
    global max_num, min_num
    if step == N:
        result = calculater(cul_list)
        if result > max_num: max_num = result
        if result < min_num: min_num = result
        return

    for i in range(4):
        if amounts[i] > 0:
            amounts[i] -= 1
            # 리스트를 새로 생성하여 넘겨줌
            solution(step + 1, cul_list + [oper_symbols[i], input_numbers[step]])
            amounts[i] += 1

# 시작
solution(1, [input_numbers[0]])

print(max_num)
print(min_num)