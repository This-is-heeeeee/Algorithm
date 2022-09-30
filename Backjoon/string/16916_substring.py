# 부분 문자열


def solution(S, P):
    if P in S:
        return 1
    return 0


if __name__ == "__main__":
    S = input()
    P = input()

    print(solution(S, P))
