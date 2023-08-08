def logged(function_name):
    def wrapper(*args):
        return f"you called {function_name.__name__}{args}\n" \
               f"it returned {function_name(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# you called func(4, 4, 4)
# it returned 6


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

# you called sum_func(1, 4)
# it returned 5
