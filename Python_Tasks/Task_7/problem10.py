s = input().strip()

count = 1 if s else 0

for ch in s:
    if ch.isupper():
        count += 1

print(count)
