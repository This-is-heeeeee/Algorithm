# 내림차순 정렬
import pytest

@pytest.mark.parametrize("N,data,expected",
                         [(3,[15,27,12],[27,15,12])])
def test(N,data,expected):
    result = solve(N,data)
    assert result == expected

def solve(N,data):
    return sorted(data, reverse=True)

