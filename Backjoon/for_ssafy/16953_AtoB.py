# A->B


def solution(A,B):
    count = 1

    while A < B:
        if B % 2 == 0:
            B /= 2
        elif B % 10 == 1:
            B = B//10
        else:
            return -1
        count += 1

    if A == B:
        return count
    else:
        return -1

if __name__ == "__main__":
    A, B = map(int, input().split())

    print(solution(A,B))
