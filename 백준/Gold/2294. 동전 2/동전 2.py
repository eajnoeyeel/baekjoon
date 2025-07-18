from cmath import inf


n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [inf] * (k + 1)
dp[0] = 0

for coin in coins:
    for amount in range(coin, k + 1):
        # dp[amount]는 i원을 만드는 방법의 수
        dp[amount] = min(dp[amount], dp[amount - coin] + 1)

if (dp[k] == inf):
    print(-1)
else:
    print(dp[k])