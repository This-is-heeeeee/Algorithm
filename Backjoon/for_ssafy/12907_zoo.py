# 동물원


def solution(N, animals):
    answer = 1
    limit = 2
    remaining_animals = N
    i = 0

    while remaining_animals > 0:
        count = animals.count(i)
        if count > limit or count == 0:
            return 0
        if count == 2:
            answer *= 2
            remaining_animals -= 2
        elif count == 1 and limit == 2:
            answer *= 2
            remaining_animals -= 1
            limit = 1
        else:
            remaining_animals -= 1
        i += 1

    return answer

    for i in range(N):
        count = animals.count(i)
        if count > limit:
            return 0
        if count == 1:
            limit = 1


if __name__ == "__main__":
    N = int(input())
    animals = list(map(int, input().split()))

    print(solution(N, animals))