class A:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, aa):
        self._a = aa
        return self._a


b = A('ah', 'aah')

print(b.a)
b.a = "kalak"

print(b.a)

