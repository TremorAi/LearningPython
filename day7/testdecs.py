__author__ = "Tremor"


def decorator(func):
    print(func)
    return func

@decorator
def OTHERFUNCT():
    print("DOG GOT BONE")

OTHERFUNCT()