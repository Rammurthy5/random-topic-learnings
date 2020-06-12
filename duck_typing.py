"""
Duck Typing is helpful in returning some value nonetheless the type / class of the object. Objective is to get something
work based on behaviour rather having dependency on type of the object.

..date..    March 25 2020
..real-time eg..    we have a len() method in Python, which can return length of string, dict, list only. what if we
                    need to return something when we do it for a class? can be doable with the help of dunders!
                    OR
                    class A dont want to have concrete dependency, & it just wanna call method B from different class /
                     interface.
                    Can be implemented with the help of duck typing / dependency injection.

https://hackernoon.com/python-duck-typing-or-automatic-interfaces-73988ec9037f
"""


class Hello:

    def __len__(self):
        """By declaring this we are making sure that len() works not based on TYPE, but based on behaviour."""
        return 1234


h = Hello()

print(len(h))       # prints 1234


# Example 2

a = 'stroiae'

l = ['ared', 'louis', 'tariq', 'ram', 'jona', 'nick']

t = ('arse', 'myarse', 'nipper', 'jeopardy')

d = {'ch':'chet'}

s = {'chet', 'chetchet', 'see', 'oral'}

# we have all the above different data types. Now we gonna write a method below to demonstrate duck-typing


def find_vowels(iterable):
    res = list()

    for i in iterable:              # this would work for any object if it behaves like an iterable. this duck-typing
#   for i in range(len(iterable)):
#       i = iterable[i]             # Had we included the above 2 lines, it would be SPECIFIC to type list / tuple. wont
                                    # work for dict / set.
        if i[0] in 'aeiou':
            res.append(i)

    return res
