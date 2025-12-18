N, M = map(int, input().split())
input_list = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if input_list[i][j] == 1:
            house.append([i, j])
        elif input_list[i][j] == 2:
            chicken.append([i, j])

min_dist = int(21e10)

def get_dist(house, chicken_shop):
    total_dist = 0
    for house_x, house_y in house:
        local_dist = int(21e10)
        for chicken_x, chicken_y in chicken_shop:
            local_dist = min(local_dist, abs(house_x - chicken_x) + abs(house_y - chicken_y))
        total_dist += local_dist
    return total_dist

def solution(start, step, chicken_shop):
    global min_dist
    if step == M:
        total_dist = get_dist(house, chicken_shop)
        min_dist = min(total_dist, min_dist)
    for i in range(start, len(chicken)):
            solution(i + 1, step + 1, chicken_shop + [chicken[i]])

solution(0, 0, [])
print(min_dist)