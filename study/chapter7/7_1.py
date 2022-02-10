# 부품찾기
import pytest

@pytest.mark.parametrize("N,parts_1,M,parts_2,expected",
                         [(5, [8, 3, 7, 9, 2], 3, [5, 7, 9], ['no', 'yes', 'yes'])])
def test(N,parts_1,M,parts_2,expected):
    result = solve(N,parts_1,M,parts_2)
    assert result == expected

def solve(N,parts_1,M,parts_2):
    result = []
    for part in parts_2:
        if part in parts_1:
            result.append('yes')
        else:
            result.append('no')

    return result