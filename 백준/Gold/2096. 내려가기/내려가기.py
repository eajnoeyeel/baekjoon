import sys
input = sys.stdin.readline

N = int(input())

prev_max = list(map(int, input().split()))
prev_min = prev_max[:]

for i in range(N - 1):
    a0, a1, a2 = prev_max
    b0, b1, b2 = prev_min

    x0, x1, x2 = map(int, input().split())

    prev_max[0] = max(a0, a1) + x0
    prev_max[1] = max(a0, a1, a2) + x1
    prev_max[2] = max(a1, a2) + x2

    prev_min[0] = min(b0, b1) + x0
    prev_min[1] = min(b0, b1, b2) + x1
    prev_min[2] = min(b1, b2) + x2

print(max(prev_max), min(prev_min))
