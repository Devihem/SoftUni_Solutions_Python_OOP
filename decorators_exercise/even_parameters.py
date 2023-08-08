def even_parameters(func):
    def wrapper(*args):
        for el in args:
            if type(el) is not int:
                return "Please use only even numbers!"
            elif int(el) % 2 != 0:
                return "Please use only even numbers!"

        else:
            return func(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
