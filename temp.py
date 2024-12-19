import time


def logger(func):
    def wrapped(*args, **kwargs):
        print(f"Calling {func.name} with arguments {args}")
        return func(*args, **kwargs)
    return wrapped
def timer(func):
    def wrapped(*args, **kwargs):
        start_time = time.time() * 1000000
        result = func(*args, **kwargs)
        end_time = time.time() * 1000000
        print(f"Execution time: {end_time - start_time} microseconds")
        return result
    return wrapped
@logger
@timer  # Note: timer is applied first, then logger
def testfn(n):
    for i in range(n):
        a = i * 10
    return "Done!"
print(testfn(1000))
