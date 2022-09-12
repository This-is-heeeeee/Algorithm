# 소수&팰린드롬


import math

def check_palindrome(N):
    string_N = str(N)
    for i in range(len(string_N)//2):
        if string_N[i] != string_N[-i-1]:
            return False

    return True

def check_prime_num(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False

    return True

def solution(N):
    if N == 1:
        return 2

    num = N
    while 1:
        if check_palindrome(num):
            if check_prime_num(num):
                return num

        num += 1

if __name__ == "__main__":
    N = int(input())

    print(solution(N))
