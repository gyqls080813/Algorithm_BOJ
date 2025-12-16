N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()

def recur(num, arr):
    if num == M:
        result = ' '.join(map(str, arr))
        print(result)
        return
    for i in range(N):
        recur(num + 1, arr + [input_list[i]])
recur(0, [])