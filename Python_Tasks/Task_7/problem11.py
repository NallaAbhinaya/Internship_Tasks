p = int(input())

for _ in range(p):
    s1 = set(input().strip())
    s2 = set(input().strip())

    if s1.intersection(s2):
        print("YES")
    else:
        print("NO")
