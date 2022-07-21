# 못생긴 수
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...

import pytest


@pytest.mark.parametrize("n, expected",
                         [(11, 15),
                          (10, 12),
                          (4, 4)])


def test(n, expected):
    answer = solution(n)
    assert answer == expected


def solution(n):
    ugly_nums = [1]
    num = 2
    while len(ugly_nums) != n:
        for ugly_num in ugly_nums:
            if ugly_num * 2 == num or ugly_num * 3 == num or ugly_num * 5 == num:
                ugly_nums.append(num)
                break

        num += 1

    result = ugly_nums[-1]
    return result