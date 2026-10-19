
# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = list(map(int, input().split()))
    shoes = Counter(shoe_sizes)

    N = int(input())
    total_earnings = 0

    for i in range(N):
        size, price = map(int, input().split())

        if shoes[size] > 0:
            total_earnings += price
            shoes[size] -= 1

    print(total_earnings)
