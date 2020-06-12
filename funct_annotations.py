"""
Function annotations are used to have type checking on python programs using 3rd party modules like mypy, pydoc, inspect.

for my example, i have stick with mypy.

..date..    25th March 2020
..usage..   mypy <fileName>.py

"""


class FunctAnnot:

    def check(self, path: str) -> int:
        pass

    def check2(self, dd: int, st: str) -> dict:
        pass


class Child(FunctAnnot):

    def check(self, path: str) -> str:
        r = 4
        return r

    def check2(self, dd: int, st: str) -> dict:
        d = {'a': 2, 'b':3}
        r = 3
        return r


c = Child()
print(c.check(7))

# Expected Output:
    # understand_metaclass.py:20: error: Return type "str" of "check" incompatible with return type "int" in supertype "FunctAnnot"
    # understand_metaclass.py:22: error: Incompatible return value type (got "int", expected "str")
    # understand_metaclass.py:27: error: Incompatible return value type (got "int", expected "Dict[Any, Any]")
    # understand_metaclass.py:31: error: Argument 1 to "check" of "Child" has incompatible type "int"; expected "str"
    # Found 4 errors in 1 file (checked 1 source file)

