def log_call(func):
    def wrapper(*args):
        print("Calling", func.__name__, "with", args)
        result = func(*args)
        print("Result:", result)
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


add(10, 20)

# Output:
# Calling add with (10, 20)
# Result: 30
