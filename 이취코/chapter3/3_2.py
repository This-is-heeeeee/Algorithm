def main():
    N, M = map(int, input().split())

    answer = 0
    for _ in range(N):
        cards = list(map(int, input().split()))
        _min = min(cards)
        answer = max(answer,_min)

    print(answer)

if __name__ == "__main__":
    main()