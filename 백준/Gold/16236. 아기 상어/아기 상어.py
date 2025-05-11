from collections import deque

N = int(input())
board = []
shark_pos = []
shark_cnt = 0
shark_size = 2
time = 0

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 9:
            shark_pos.append(r)
            shark_pos.append(c)
            row[c] = 0
    board.append(row)


def bfs(x, y, d, graph):
    global shark_pos, shark_cnt, shark_size, time

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(d, x, y)])
    visited = set([(x, y)])

    fishes = []
    while queue:
        d, x, y = queue.popleft()
        for idx in range(4):
            nd = d + 1
            nx = x + dx[idx]
            ny = y + dy[idx]

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]):
                continue
            if graph[nx][ny] > shark_size:
                continue
            if (nx, ny) in visited:
                continue
            if 0 < graph[nx][ny] < shark_size:
                fishes.append((nd, nx, ny))
            
            visited.add((nx, ny))
            queue.append((nd, nx, ny))
    
    if not fishes:
        return False
    fishes.sort()
    # 아기 상어가 이동할 좌표
    chosen = fishes[0]
    # 해당 자리로 아기 상어 이동
    shark_pos[0], shark_pos[1] = chosen[1], chosen[2]
    # 해당 자리의 물고기 섭취
    time += chosen[0]
    board[chosen[1]][chosen[2]] = 0
    shark_cnt += 1
    if shark_cnt == shark_size:
        shark_size += 1
        shark_cnt = 0
    return True
    

def solution():
    global time
    while (1):
        if not bfs(shark_pos[0], shark_pos[1], 0, board):
            return time
    

if __name__ == "__main__":
    print(solution())