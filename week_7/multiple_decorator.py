import time
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args):
        print("Calling", func.__name__)
        result = func(*args)
        print("Result:", result)
        return result

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args):
        start = time.time()

        result = func(*args)

        end = time.time()

        print("Time taken:", end - start, "seconds")
        return result

    return wrapper


@log_call
@timer
def add(a, b):
    return a + b


add(10, 20)

# Output:
# Calling add
# Result: 30
# Time taken: 0.00000... seconds
