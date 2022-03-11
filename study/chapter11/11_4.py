# 만들 수 없는 금액
import pytest

@pytest.mark.parametrize("N,coins,expected",
                         [(5, [3, 2, 1, 1, 9], 8)])
def test(N,coins,expected):
    answer = solve(N,coins)
    assert answer == expected

def solve(N,coins):
    sub_lists = []
    amounts = [False for _ in range(sum(coins) + 1)]
    for i in range(len(coins) + 1):
        for j in range(i):
            sub_lists.append(coins[j:i])

    for sub in sub_lists:
        amounts[sum(sub)] = True

    for i in range(1, len(amounts)):
        if not amounts[i]:
            return i
