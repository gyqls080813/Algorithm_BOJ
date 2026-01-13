A, B = map(int, input().split())
result = -1
step = 1
greedy = B

while greedy > A:

    if greedy % 2 == 0:
        greedy //= 2
        step += 1

    elif greedy % 10 == 1:
        greedy //= 10
        step += 1
    else:
        break

if greedy == A:
    result = step
print(result)