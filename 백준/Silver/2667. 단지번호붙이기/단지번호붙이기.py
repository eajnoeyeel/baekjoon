import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_x, start_y, N, graph, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    # 시작하는 집 한 채를 미리 카운트
    count = 1


    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1

    return count


def main():
    N = int(input())
    graph = []

    for _ in range(N):
        graph.append(list(map(int, input().strip())))
    
    # 1. 전체 방문 체크 배열을 여기서 선언
    visited = [[False] * N for _ in range(N)]
    results = []

    for row in range(N):
        for col in range(N):
            # 2. 집이 있고 아직 방문 안 한 곳에서만 BFS 시작
            if graph[row][col] == 1 and not visited[row][col]:
                results.append(bfs(row, col, N, graph, visited))
    
    # 3. 총 단지 수와 각 단지 내 집 수를 오름차순 출력
    print(len(results))
    for res in sorted(results):
        print(res)


if __name__ == "__main__":
    main()