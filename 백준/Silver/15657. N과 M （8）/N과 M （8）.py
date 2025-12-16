N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()

def recur(num, arr, start):
    if num == M:
        result = ' '.join(map(str, arr))
        print(result)
        return
    for i in range(start, N):
        recur(num + 1, arr + [input_list[i]], i)
recur(0, [], 0)