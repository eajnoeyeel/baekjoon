from heapq import heappush, heappop

N = int(input())
problems = []

for _ in range(N):
    d, r = map(int, input().split())
    problems.append((d, r))

problems.sort()

heap = []
for d, r in problems:
    heappush(heap, r)
    if len(heap) > d:
        heappop(heap)

print(sum(heap))
