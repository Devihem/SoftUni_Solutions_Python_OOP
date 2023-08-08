def squares(n):
    current_number = 1

    while current_number < n + 1:
        yield current_number * current_number
        current_number += 1


print(list(squares(5)))