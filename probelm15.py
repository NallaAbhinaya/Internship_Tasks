
n = int(input())

word_count = {}

for i in range(n):
    word = input().strip()
    word_count[word] = word_count.get(word, 0) + 1

print(len(word_count))
print(*word_count.values())
