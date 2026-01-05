N = int(input())
input_list = list(map(int, input().split()))
result = [0] * N

stack = []

for idx, value in enumerate(input_list):
    if not stack:
        stack.append([idx, value])
    else:
        if stack[-1][1] < value:
            while stack and stack[-1][1] <= value:
                stack.pop()
            if not stack:
                stack.append([idx, value])
                continue
            result[idx] = stack[-1][0] + 1
            stack.append([idx, value])
        else:
            result[idx] = stack[-1][0] + 1
            stack.append([idx, value])

print(' '.join(map(str, result)))