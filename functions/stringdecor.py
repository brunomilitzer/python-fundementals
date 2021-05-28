def decorfun(fun):
    def inner(n):
        result = fun(n)
        result = result + " How are you?"
        return result
    return inner


@decorfun
def hello(name):
    return "Hello " + name


print(hello("Bruno"))
