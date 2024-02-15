def repeat_hello_decorator(func):
    def wrapper():
        x = int(input("Enter a number of repetitions: "))
        for _ in range(x):
            func()
    return wrapper

@repeat_hello_decorator
def hello():
    print('Hello')


hello()
