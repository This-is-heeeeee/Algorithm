# 소수 부분 문자열


import math

def solution(string):
    maximum = 0
    checked = []
    for start_idx in range(len(string)):
        for end_idx in range(start_idx, len(string)):
            num = int(string[start_idx:end_idx+1])
            if num < 2 or num > 100000:
                continue
            if num in checked:
                continue
            checked.append(num)

            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    break
            else:
                if maximum < num:
                    maximum = num
    return maximum


if __name__ == "__main__":
    while 1:
        num = input()
        if num == '0':
            break

        print(solution(num))
