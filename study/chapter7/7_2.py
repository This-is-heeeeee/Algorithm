# 떡볶이 떡 만들기
import pytest

@pytest.mark.parametrize("N,M,data,expected",
                         [(4, 6, [19, 15, 10, 17], 15)])
def test(N, M, data, expected):
    result = solve(N, M, data)
    assert result == expected

def solve(N, M, data):
    remain = 0
    idx = int(max(data)/2)

    while remain != M:
        remain = 0
        for d in data:
            if d > idx:
                remain += d - idx
        if remain < M:
            idx -= 1
        elif remain > M:
            idx += 1
        else:
            break

    return idx