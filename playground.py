# *args use to take unlimited number of argument
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1, 2, 3, 4, 4)
