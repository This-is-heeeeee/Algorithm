# 무지의 먹방 라이브
# 이진 탐색(binary search)
import pytest

@pytest.mark.parametrize("food_times,k,expected",
                         [([3, 2, 1, 1], 9, -1)])
def test(food_times,k,expected):
    answer = solution(food_times,k)
    assert answer == expected


def solution(food_times, k):
    answer = -1

    if sum(food_times) <= k:
        return answer

    low, high = 0, max(food_times)
    length = len(food_times)
    rounds, idx = 0, 0
    while low <= high:
        mid = (low + high) // 2
        last = mid * length  # 마지막 음식을 먹을때의 시간
        for ft in food_times:
            temp = ft - mid
            if temp < 0:
                last += temp

        if k < last:
            high = mid - 1
        else:
            rounds = mid
            idx = last
            low = mid + 1

    food_times = [ft - rounds for ft in food_times]

    for i in range(length):
        if idx == k and food_times[i] > 0:
            return i + 1
        if food_times[i] > 0:
            idx += 1

    return answer