N = int(input())
M = int(input())
bus = []
for _ in range(M):
    bus_t = list(map(int, input().split()))
    bus.append(bus_t)

start, end = map(int, input().split())

graph = [[] * N for _ in range(N + 1)]

for st, ed, cost in bus:
    graph[st].append([cost, ed])

min_cost = int(21e10)

from heapq import heappop, heappush

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [int(21e10)] * (N + 1)
    while pq:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    return dists

result = dijkstra(start)
print(result[end])
