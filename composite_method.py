"""
To understand & demonstrate composition. its an alternate approach to inheritance. to use only one or two methods
from a class, we can avoid inheritance, and go with composition

..date..    march 25 2020
..additional ..     Understand the importance of total_ordering from functools module
"""

class A:

    persist = ['get', 'hey', 'cha']
    aa = 2
    def __init__(self, instance):
        print("init")
        self._instance = instance

    def __enter__(self):
        print("enter")

    def __getattr__(self, item):
        print("searching")
        if item in self.persist:
            return getattr(self._instance, item)

    def get(self):
        print("inner get")


from functools import total_ordering

@total_ordering         # this will make sure we implement at least one ordering dunder operation: < > <= >=
class B:

    aa = 1
    def get(self):
        print("composite get")

    def hey(self):
        print("composite get")

    def cha(self):
        print("composite get")

    def set(self):
        print("composite get")

    def __eq__(self, other):
        print("in here")
        return self.aa == other.aa

    def __lt__(self, other):
        return self.aa < other.aa

b = B()
a = A(b)            # passing class B's instance 'b' here rather inheriting it. this will invoke __getattr__ &
                    # do the needful
print(a == b)
a.hey()
a.set()