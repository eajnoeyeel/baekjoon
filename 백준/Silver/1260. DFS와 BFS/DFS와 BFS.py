from collections import deque

N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
result = []

def dfs(node):
    visited[node] = True
    result.append(node)

    for next in sorted(graph[node]):
        if not visited[next]:
            dfs(next)

    return result

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for next in sorted(graph[node]):
            if not visited[next]:
                visited[next] = True
                queue.append(next)

    return result

dfs_result = dfs(start)
bfs_result = bfs(start)
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))