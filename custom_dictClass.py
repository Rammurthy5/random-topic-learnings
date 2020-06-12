"""
Creating a dict class where that returns a dict-like object itself.
"""

class Dictionary:
    def __init__(self, a, b):

        super(Dictionary, self).__init__()
        self.a = a
        self.b = b
        self.c = []
        self.d = dict()

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)


d = Dictionary('A', 'B')
d['c'].append(9)
d['d']['key1']="HEY"
print(d['d']['key1'])

