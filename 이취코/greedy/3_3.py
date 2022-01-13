from math import log, pow

def main():
    N, K = map(int, input().split())

    a = int(log(N, K))
    b = int(N - pow(K,a))
    answer = a + b

    print(answer)

if __name__ == "__main__":
    main()