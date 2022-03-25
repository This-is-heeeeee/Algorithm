# 외벽 점검
# 22/25(88)
import pytest

@pytest.mark.parametrize("n, weak, dist, expected",
                         [(12, [1, 5, 6, 10], [1, 2, 3, 4], 2),
                          (12, [1, 3, 4, 9, 10], [3, 5, 7], 1),
                          (30, [0,3,11,21],[10,4],2)])
def test(n, weak, dist, expected):
    answer = solution(n, weak, dist)
    assert answer == expected


def inspection(weak,dist,start,weak_dist, clockwise):
    weak_tmp1 = weak.copy()
    weak_tmp2 = weak.copy()
    sum = 0
    i = start
    if clockwise == 1:
        i = (i + len(weak)-1) % len(weak)
    dist_temp = dist.copy()
    friends = 0
    while True:
        weak_tmp2.remove(weak_tmp1[i])
        if not dist_temp:
            friends = -1
            break
        if not weak_tmp2:
            dist_temp.pop(-1)
            friends = len(dist) - len(dist_temp)
            break
        sum += weak_dist[i]

        if dist_temp[-1] < sum:
            remove_idx = 0
            for idx, d in enumerate(dist_temp):
                if d >= sum - weak_dist[i] and d < sum:
                    remove_idx = idx
                    break
            dist_temp.pop(remove_idx)
            friends = len(dist) - len(dist_temp)
            sum = 0

        if clockwise == 0:
            i = (i + 1) % len(weak)
        else:
            i = (i + len(weak) - 1) % len(weak)
    return friends


def solution(n, weak, dist):
    answer = -1

    max_weak_dist = 0
    start = 0
    weak_dist = [0 for _ in range(len(weak))]
    for i in range(len(weak)):
        weak_dist[i] = weak[(i+1)%len(weak)] - weak[i]
        if weak_dist[i] > n//2:
            weak_dist[i] = weak[i] + n - weak[(i + 1) % len(weak)]
        elif weak_dist[i] < 0:
            weak_dist[i] = weak[(i+1)%len(weak)] + n - weak[i]

        if max_weak_dist < weak_dist[i]:
            max_weak_dist = weak_dist[i]
            start = (i+1)%len(weak)

    dist.sort()

    clockwise = inspection(weak,dist,start,weak_dist, 0)
    reverse_clockwise = inspection(weak,dist,start,weak_dist, 1)

    if clockwise == -1 and reverse_clockwise == -1:
        answer = -1
    elif clockwise == -1 or reverse_clockwise == -1:
        answer = max(clockwise, reverse_clockwise)
    else:
        answer = min(clockwise, reverse_clockwise)

    return answer