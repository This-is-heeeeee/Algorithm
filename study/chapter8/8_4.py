# 효율적인 화폐 구성
# 주어진 화폐로 M원을 만드는 최소 개수
import pytest

@pytest.mark.parametrize("N,M,coins,expected",
                         [(2, 15, [2,3], 5)])   #(3, 4, [3, 5, 7], -1)])
def test(N,M,coins,expected):
    solve(M, coins, 0)
    assert dp[M] == expected

dp = [-1 for _ in range(10001)]
dp[0] = 0

def solve(M, coins, i):
    for coin in coins:
        if i+coin <= M and (dp[i + coin] > dp[i] or dp[i + coin] == -1):
            dp[i + coin] = dp[i] + 1
            solve(M, coins, i + coin)
