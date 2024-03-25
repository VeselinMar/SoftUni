class store_results:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):  # works as wrapper
        with open("log.txt", "a") as log_file:
            log_file.write(
                f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}\n"
            )


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
