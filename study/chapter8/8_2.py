# 개미전사
# 최대로 갖고 올 수 있는 식량
import pytest

@pytest.mark.parametrize("N,K,expected",
                         [(4,[1,3,1,5],8)])
def test(N,K,expected):
    dp[0] = K[0]
    dp[1] = K[1]
    solve(N, K, 0)
    solve(N, K, 1)
    result = max(dp[N-1],dp[N-2])
    assert result == expected

dp = [0 for _ in range(101)]

def solve(N, K, i):
    if i + 2 <= N-1 and (dp[i+2] > dp[i] or dp[i+2] == 0):
        dp[i+2] = dp[i] + K[i+2]
        solve(N, K, i+2)
    if i + 3 <= N-1 and (dp[i+3] > dp[i] or dp[i+3] == 0):
        dp[i+3] = dp[i] + K[i+3]
        solve(N, K, i+3)

