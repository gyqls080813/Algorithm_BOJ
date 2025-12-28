from heapq import heappop, heappush
N, M = map(int, input().split())
board = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    board[start].append((weight, end))
    board[end].append((weight, start))
INF = int(21e8)

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (N + 1)
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)
        if dists[node] < dist:
            continue
        for next_dist, next_node in board[node]:
            new_dist = next_dist + dist
            if dists[next_node] <= new_dist:
                continue 

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    return dists

v1, v2 = map(int, input().split())
dist_from_1  = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

ans = min(path1, path2)
print(ans if ans < INF else -1)