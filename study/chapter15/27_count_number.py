# 정렬된 배열에서 특정 수의 개수 구하기

import pytest


@pytest.mark.parametrize("n,x,nums,expected",
                         [(7, 2, [1, 1, 2, 2, 2, 2, 3], 4),
                          (7, 4, [1, 1, 2, 2, 2, 2, 3], -1)])

def test(n, x, nums, expected):
    answer = solution(x, nums)
    assert answer == expected

def solution(x, nums):
    answer = nums.count(x)
    if answer <= 0:
        answer = -1
    return answer

