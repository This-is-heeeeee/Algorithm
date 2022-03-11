# 곱하기 혹은 더하기
import pytest

@pytest.mark.parametrize("S,expected",
                         [("02984", 576),
                          ("567", 210)])
def test(S,expected):
    answer = solve(S)
    assert answer == expected

def solve(S):
    I = [int(s) for s in S]
    answer = 0
    for i in I:
        if i == 0 or answer == 0:
            answer += i
        else:
            answer *= i

    return answer
