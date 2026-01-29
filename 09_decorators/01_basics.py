# Decorators let you add extra functionality to a function
# without editing the function itself.

def decorator_func(original_func):
    def wrapper():
        print("Something before the function runs")
        original_func()
        print("Something after the function runs")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()
