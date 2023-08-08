def vowel_filter(function):
    def wrapper():
        vowel_list = [x for x in function() if x.lower() in ["e", "y", "u", "i", "o", "a"]]

        return vowel_list
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
