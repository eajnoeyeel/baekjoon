import sys
from collections import deque
input = sys.stdin.readline


def bfs(start_x, start_y, end_x, end_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(graph), len(graph[0])

    queue = deque([(start_x, start_y, 1)])
    visited = set([(start_x, start_y)])

    while queue:
        x, y, dist = queue.popleft()

        if x == end_x and y == end_y:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited:
                    if graph[nx][ny] == 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))

    return -1


def main():
    N, M = map(int, input().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().strip())))

    print(bfs(0, 0, N - 1, M - 1, graph))
    

if __name__ == "__main__":
    main()