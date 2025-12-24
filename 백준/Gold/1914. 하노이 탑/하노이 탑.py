N = int(input())
route = []
def solution(start, end, number):
    if number == 1:
        print(start, end)
        return
    solution(start, 6 - start - end, number - 1)
    print(start, end)
    solution(6 - start - end, end, number - 1)

print((1<<N) - 1)
if N <= 20:
    solution(1, 3, N)