import sys
from collections import Counter
input = sys.stdin.readline

def main():
    n = int(input())
    cards = list(map(int, input().split()))
    m = int(input())
    qs = list(map(int, input().split()))
    
    cnt = Counter(cards)
    res = []
    for q in qs:
        res.append(str(cnt[q]))
    print(" ".join(res))


if __name__ == "__main__":
    main()