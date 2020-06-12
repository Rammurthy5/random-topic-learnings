"""
New stuff in Python generators
    send(), throw(), yield from, return

..date..    Apr 13 2020
"""

# Typical Generator


def gen1():

    yield "i am"
    # for i in range(5):
    #     yield i
    return "final"

# g = gen1()

# New-gen Generators


def gen2():
    # for j in range(5, 10):
    #     yield j
    yield 1

    val = yield from gen1()
    print("value ", val)
    yield 4


g2 = gen2()

# ele = next(g2)
# while ele:
#     print(ele)
#     ele = next(g2)
print(next(g2))
print(next(g2))
# print(next(g2))
print(g2.send('abc'))
