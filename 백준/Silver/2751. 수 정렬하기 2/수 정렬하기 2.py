import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()

output = sys.stdout.write
for x in arr:
    output(str(x) + '\n')
