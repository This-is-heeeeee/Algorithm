# 고정점 찾기
# 시간초과 날 듯..?

import pytest


@pytest.mark.parametrize("n,nums,expected",
                         [(5, [-15, -6, 1, 3, 7], 3),
                          (7, [-15, -4, 2, 8, 9, 13, 15], 2),
                          (7, [-15, -4, 3, 8, 9, 13, 15], -1)])

def test(n, nums, expected):
    answer = solution(nums)
    assert answer == expected

def binary_search(nums, idx):
    i = len(nums)//2
    if nums[i] == idx:
        return idx
    elif len(nums) == 1:
        return -1
    elif nums[i] > idx:
        left_side = nums[0:i]
        return binary_search(left_side, idx - (len(left_side)//2 + 1))
    else:
        right_side = nums[i+1:]
        return binary_search(right_side, idx + (len(right_side) // 2 + 1))

def solution(nums):
    idx = len(nums)//2
    result = binary_search(nums, idx)
    return result
