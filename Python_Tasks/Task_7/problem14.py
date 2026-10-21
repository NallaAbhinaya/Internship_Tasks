from collections import Counter

q = int(input())

for _ in range(q):
    s = input().strip()
    n = len(s)

    if n % 2 != 0:
        print(-1)
    else:
        first = s[:n // 2]
        second = s[n // 2:]

        count1 = Counter(first)
        count2 = Counter(second)

        changes = 0

        for ch in count1:
            changes += max(0, count1[ch] - count2[ch])

        print(changes)
