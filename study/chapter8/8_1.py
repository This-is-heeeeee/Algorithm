# 1로 만들기
import pytest

@pytest.mark.parametrize("X,expected",
                         [(26,3)])
def test(X,expected):
    solve(X)
    assert dp[1] == expected

dp = [0 for _ in range(30001)]

def solve(X):
    if X % 5 == 0 and (dp[int(X/5)] > dp[X] or dp[int(X/5)] == 0):
        dp[int(X/5)] = dp[X] + 1
        solve(int(X/5))
    if X % 3 == 0 and (dp[int(X/3)] > dp[X] or dp[int(X/3)] == 0):
        dp[int(X/3)] = dp[X] + 1
        solve(int(X/3))
    if X % 2 == 0 and (dp[int(X/2)] > dp[X] or dp[int(X/2)] == 0):
        dp[int(X / 2)] = dp[X] + 1
        solve(int(X/2))
    if X > 1 and (dp[X-1] > dp[X] or dp[X-1] == 0):
        dp[X - 1] = dp[X] + 1
        solve(X-1)
