def make_bold(func):
    def wrapper(*args):
        text = func(*args)
        return f'<b>{text}</b>'

    return wrapper


def make_italic(func):
    def wrapper(*args):
        text = func(*args)
        return f'<i>{text}</i>'

    return wrapper


def make_underline(func):
    def wrapper(*args):
        text = func(*args)
        return f'<u>{text}</u>'

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
