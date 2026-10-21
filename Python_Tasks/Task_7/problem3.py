s = input().strip()
expected = "SOS"
count = 0

for i in range(len(s)):
    if s[i] != expected[i % 3]:
        count += 1

print(count)
