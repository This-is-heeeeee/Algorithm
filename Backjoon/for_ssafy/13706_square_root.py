# 제곱근


def solution(num):
    low = 0
    high = num//2
    mid = (low + high) // 2

    while mid*mid != num:
        tmp = mid*mid
        if tmp < num:
            low = mid + 1
            mid = (low + high) // 2
        elif tmp > num:
            high = mid - 1
            mid = (low + high) // 2

    return mid

if __name__ == "__main__":
    num = int(input())

    print(solution(num))