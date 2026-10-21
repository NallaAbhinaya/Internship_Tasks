q = int(input())

for _ in range(q):
    s = input().strip()
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1

    print(deletions)
