t = int(input())

for _ in range(t):
    s = input().strip()
    r = s[::-1]

    funny = True

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(r[i]) - ord(r[i - 1])):
            funny = False
            break

    print("Funny" if funny else "Not Funny")
