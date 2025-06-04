def dfs(index):
    global max_broken

    # 종료 조건
    if index == N:
        broken = sum(1 for d in durability if d <= 0)
        max_broken = max(max_broken, broken)
        return

    # 현재 계란이 깨졌거나, 칠 수 있는 계란이 없으면 다음으로 넘어감
    if durability[index] <= 0 or all(durability[i] <= 0 or i == index for i in range(N)):
        dfs(index + 1)
        return

    for i in range(N):
        if i != index and durability[i] > 0:
            # 타격 전 상태 저장
            s1, s2 = durability[index], durability[i]

            # 내구도 갱신
            durability[index] -= weight[i]
            durability[i] -= weight[index]

            # 다음 계란으로
            dfs(index + 1)

            # 상태 복구
            durability[index], durability[i] = s1, s2


def main():
    global N, durability, weight, max_broken

    N = int(input())
    durability = []
    weight = []
    for _ in range(N):
        d, w = map(int, input().split())
        durability.append(d)
        weight.append(w)

    max_broken = 0
    dfs(0)
    print(max_broken)


if __name__ == "__main__":
    main()