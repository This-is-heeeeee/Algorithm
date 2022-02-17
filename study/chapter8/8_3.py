# 바닥공사
# 타일을 깔 수 있는 경우의 수
import pytest

@pytest.mark.parametrize("N,expected",
                         [(3, 5)])
def test(N,expected):
    dp[1] = 1
    dp[2] = 2
    solve(N, 1)
    assert dp[N]%796796 == expected

dp = [0 for _ in range(1001)]

def solve(N, i):
    if i + 1 <= N:
        dp[i+1] += dp[i]
        solve(N, i + 1)
    if i +2 <= N:
        dp[i+2] += (2*dp[i])
        solve(N, i + 2)