def print_row(n, count):
    print(' ' * (n - count), end="")
    print(*['*'] * count)


def print_rhombus(n):
    for count in range(1, n + 1):
        print_row(n, count)

    for count in range(n - 1, 0, -1):
        print_row(n, count)


n = int(input())
print_rhombus(n)
