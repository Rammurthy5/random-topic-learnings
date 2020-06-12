"""
Metaclass are the blueprint for Python 'class' ie, python 'class' inherits 'type', which is known as meta class.
These concepts are used if you want to tweak the way your class behaves normally.

..date..    March 25, 2020
..real-time eg..    Say you want a variable "abcd" to be set as 200 everytime you create a new class in your project.
                    we can do that by creating a new 'so-called meta' class inheriting 'type' and then tweak some dunder
                     methods inside.
                    and, whenever you create a new normal class after that, just pass metaclass='so-called-meta' as class arg.
                    you're done! Refer Eg 4

https://realpython.com/python-metaclasses/
"""

# syntax would be type(<className>, <tuple of BaseClass if there is something to inherit>, <dict of attributes if any>)


# Eg. 1

b = type('Barr', (), {'a':100})

bb = b()

print(type(bb), type(b), type(bb.__class__))


# Eg 2  Normal class creation

class Bar:

    pass


barObj = Bar()

print(type(Bar), type(barObj), type(barObj.__class__))


# Eg 3 inheritance through metaclass style

b2 = type('Barre', (b,), {'b':100})

barObj2 = b2()

print(barObj2.a, barObj2.b)


# Eg 4
# I am gonna create a metaclass 'Meta' because i want to tweak normal behaviour of classes i create for business logic
# in my projects henceforth

class Meta(type):   # we are inheriting 'type' here as we cant modify 'type' itself. so treating 'Meta' as metaclass

    def __new__(cls, *args, **kwargs):
        print("i am invoked")
        x = super().__new__(cls, *args, **kwargs)
        x.aa = 100
        return x


class NormalClass(metaclass=Meta):

    pass


n = NormalClass()
print(n.aa)         # gives 100 as assigned in metaclass 'Meta' thats the magic of metaclasses.
