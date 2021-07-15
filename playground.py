# *args use to take unlimited number of argument
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#
#
# add(1, 2, 3, 4, 4)

# kwargs

def calculate(n, **kwargs):
    print(kwargs) # prints dictionary {'add': 3, 'multiply': 2}
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
