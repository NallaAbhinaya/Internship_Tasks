n = int(input())
s = input().strip()

count = 0
i = 0

while i < n - 2:
    if s[i:i + 3] == "010":
        count += 1
        i += 3
    else:
        i += 1

print(count)
