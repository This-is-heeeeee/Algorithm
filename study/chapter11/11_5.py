# 볼링공 고르기
import pytest

@pytest.mark.parametrize("N,M,K,expected",
                         [(5,3,[1,3,2,3,2], 8),
                          (8,5,[1,5,4,3,2,4,5,2],25)])
def test(N,M,K,expected):
    answer = solve(N,M,K)
    assert answer == expected

def solve(N,M,K):
    count = 0

    for i in range(len(K)-1):
        for j in range(i+1, len(K)):
            if K[i] != K[j]:
                count += 1

    return count
