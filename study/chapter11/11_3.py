# 문자열 뒤집기
import pytest

@pytest.mark.parametrize("S,expected",
                         [("0001100", 1)])
def test(S,expected):
    answer = solve(S)
    assert answer == expected

def solve(S):
    before = ''
    count = 0
    for s in S:
        if s != before:
            before = s
            count += 1

    return count // 2
