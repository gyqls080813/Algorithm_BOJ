N = int(input())

def is_good(seq):
    L = len(seq)
    for k in range(1, L // 2 + 1):
        if seq[-k:] == seq[-2*k:-k]:
            return False
    return True

def solution(step, cum_num):
    if step == N:
        print(''.join(map(str, cum_num)))
        exit()

    for i in range(1, 4):
        cum_num.append(i)
        if is_good(cum_num):
            solution(step + 1, cum_num)
        cum_num.pop()

solution(0, [])