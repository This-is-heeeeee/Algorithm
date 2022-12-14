# ATM


def solution(P):
    P.sort()
    answer = 0

    length = len(P)

    for i, p in enumerate(P):
        answer = answer + (p*(length - i))

    return answer


if __name__ == "__main__":
    N = int(input())
    P = list(map(int, input().split()))

    print(solution(P))
