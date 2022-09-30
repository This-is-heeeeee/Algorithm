# 전화번호부
import sys

if __name__ == "__main__":
    test_case = int(sys.stdin.readline())

    for _ in range(test_case):
        n = int(sys.stdin.readline())
        the_white_pages = []
        for i in range(n):
            phone_num = sys.stdin.readline().rstrip()
            the_white_pages.append(phone_num)

        the_white_pages.sort(key=len)
        check = {}
        for phone_num in the_white_pages:
            check_tmp = check
            for num in phone_num:
                if num in check_tmp:
                    check_tmp = check_tmp[num]
                else:
                    check_tmp[num] = {}
                    check_tmp = check_tmp[num]
                if 'end' in check_tmp:
                    break
            else:
                check_tmp['end'] = True
                continue
            break
        else:
            print('YES')
            continue
        print('NO')