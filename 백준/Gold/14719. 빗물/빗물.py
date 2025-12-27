H, W = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = W - 1
left_max = 0
right_max = 0
result = 0

while left < right:
    if arr[left] < arr[right]:
        left_max = max(left_max, arr[left])
        result += left_max - arr[left]
        left += 1
    else:
        right_max = max(right_max, arr[right])
        result += right_max - arr[right]
        right -= 1

print(result)
