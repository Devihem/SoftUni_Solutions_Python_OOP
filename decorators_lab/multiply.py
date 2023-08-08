def multiply(times):
    def decorator(function):
        def wrapper(num):
            func_res = function(num) * times
            return func_res
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
