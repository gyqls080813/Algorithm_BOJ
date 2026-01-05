N = int(input())
input_list = []
for i in range(N):
    W, H = map(int, input().split())
    input_list.append((min(W, H), max(W, H)))

input_list.sort(reverse=True)

result = [1] * N

for i in range(1, N):
    max_count = result[i]
    for j in range(i):
        if input_list[i][0] <= input_list[j][0] and input_list[i][1] <= input_list[j][1]:
            max_count = max(max_count, result[j] + 1)
    result[i] = max_count

print(max(result))