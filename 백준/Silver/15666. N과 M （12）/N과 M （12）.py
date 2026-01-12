N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
new_list = []
for i in input_list:
    if i not in new_list:
        new_list.append(i)

def solution(step, start, step_list):
    if step == M:
        print(' '.join(map(str, step_list)))
        return
    for i in range(start, len(new_list)):
        solution(step + 1, i, step_list + [new_list[i]])
solution(0, 0, [])