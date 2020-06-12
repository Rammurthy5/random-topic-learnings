"""
Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object
oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate
and more elegant solutions
"""


def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"))


def times(x):
    def multiplier(y):
        print(x*y)
    return multiplier     # Returns function printer without paranthesis. This is closure.

times3 = times(3)

times3(4)