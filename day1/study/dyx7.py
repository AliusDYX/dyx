# 简单装饰器
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 带参数的装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
#dyx thinks his teacher is so so good!
@repeat(3)
def greet(name):
    print(f"Hi, {name}!")
#dyx thinks his teacher is handsome
greet("Alice")
##