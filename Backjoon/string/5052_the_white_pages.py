# 전화번호부
import sys

def solution(n, the_white_pages):

    for i in range(n-1):
        len_num = len(the_white_pages[i])
        if the_white_pages[i] == the_white_pages[i+1][:len_num]:
            return 'NO'

    return 'YES'

if __name__ == "__main__":
    test_case = int(sys.stdin.readline())

    for _ in range(test_case):
        n = int(sys.stdin.readline())
        the_white_pages = []
        for i in range(n):
            phone_num = sys.stdin.readline().rstrip()
            the_white_pages.append(phone_num)

        the_white_pages.sort()

        print(solution(n, the_white_pages))