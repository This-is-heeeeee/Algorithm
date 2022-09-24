# 회문은 회문 아니야!


#1. 문자열 전체가 회문이 아니면 문자열 길이
#2. 문자열 전체가 회문일 때, 두가지 경우
#2_1. 모두 같은 문자라면 -1
#2_2. 아니라면 문자 하나만 지워도 회문x -> 문자열 길이 -1


def check_palindrome(N):
    string_N = str(N)
    for i in range(len(string_N)//2):
        if string_N[i] != string_N[-i-1]:
            return False

    return True

def solution(S):

    if check_palindrome(S):
        S = S[:-1]
        if check_palindrome(S):
            return -1

    return len(S)

if __name__ == "__main__":
    S = input()

    print(solution(S))
