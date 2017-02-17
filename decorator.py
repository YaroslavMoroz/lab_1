def decorator(func):
    def wrapper():
        print("Yaroslav")
        return func()
    return wrapper()


@decorator
def say():
    print("Moroz")