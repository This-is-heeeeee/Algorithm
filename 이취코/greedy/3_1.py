def main():
    N,M,K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)

    answer = 0
    temp = nums[0]*K + nums[1]
    count1 = M / (K+1)
    count2 = M % (K + 1)

    answer += temp * count1
    answer += nums[0] * count2

    print(int(answer))

if __name__ == "__main__":
    main()