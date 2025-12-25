N = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

tree = [[] for _ in range(N)]
root = -1

for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        tree[parent[i]].append(i)

removed = [False] * N

def dfs_delete(node):
    removed[node] = True
    for child in tree[node]:
        dfs_delete(child)

dfs_delete(remove_node)

result = 0
for i in range(N):
    if removed[i]:
        continue

    is_leaf = True
    for child in tree[i]:
        if not removed[child]:
            is_leaf = False
            break

    if is_leaf:
        result += 1

print(result)