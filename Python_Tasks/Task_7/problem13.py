from collections import Counter

s = input().strip()
freq = Counter(Counter(s).values())

if len(freq) == 1:
    print("YES")
elif len(freq) == 2:
    items = list(freq.items())
    (f1, c1), (f2, c2) = items

    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        print("YES")
    elif abs(f1 - f2) == 1 and (
        (f1 > f2 and c1 == 1) or
        (f2 > f1 and c2 == 1)
    ):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
