import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = letters[size - 1:size - i - 1:-1]
        right = letters[size - i - 1:size]
        row = "-".join(left + right)
        lines.append(row.center(4 * size - 3, "-"))

    for line in lines[::-1]:
        print(line)

    for line in lines[1:]:
        print(line)

n = int(input())
print_rangoli(n)
