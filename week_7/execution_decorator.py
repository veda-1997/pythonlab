import time

def timer(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print("Time taken:", end - start, "seconds")

    return wrapper


@timer
def calculate():
    total = 0
    for i in range(100000):
        total = total + i

    print("Sum:", total)


calculate()

# Output:
# Sum: 4999950000
# Time taken: 0.00... seconds
