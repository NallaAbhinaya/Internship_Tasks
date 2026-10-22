
s = input().strip()
n = int(input())

weights = set()
current_weight = 0
previous_char = ""

for ch in s:
    if ch == previous_char:
        current_weight += ord(ch) - ord('a') + 1
    else:
        current_weight = ord(ch) - ord('a') + 1

    weights.add(current_weight)
    previous_char = ch

for _ in range(n):
    x = int(input())
    if x in weights:
        print("Yes")
    else:
        print("No")
