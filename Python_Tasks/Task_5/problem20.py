
# Problem: Piling Up!
# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        blocks = deque(map(int, input().split()))

        while len(blocks) > 1:
            if blocks[0] >= blocks[-1]:
                largest = blocks.popleft()
            else:
                largest = blocks.pop()

            if len(blocks) > 0 and max(blocks) > largest:
                print("No")
                break
        else:
            print("Yes")
