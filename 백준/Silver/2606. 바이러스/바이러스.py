import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, graph, num_of_computers):
    queue = deque([start])
    count = 0
    visited = [False] * (num_of_computers + 1)
    visited[start] = True

    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                count += 1
    
    return count


def main():
    num_of_computers = int(input())
    num_of_edges = int(input())

    graph = [[] for _ in range(num_of_computers + 1)]
    for _ in range(num_of_edges):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    print(bfs(1, graph, num_of_computers))


if __name__ == "__main__":
    main()