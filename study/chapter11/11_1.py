# 모험가 길드
# 모험가들로 만들 수 있는 파티의 수
import pytest

@pytest.mark.parametrize("N,panic,expected",
                         [(5,[2, 3, 1, 2, 2], 2)])
def test(N,panic,expected):
    answer = solve(N,panic)
    assert answer == expected

def solve(N,panic):
    parties = 0
    panic.sort(reverse=True)
    max_panic = 0
    for p in panic:
        if max_panic == 0:
            max_panic = p - 1
            parties += 1
        else :
            max_panic -= 1
            continue

    return parties
