"""
This is to understand how memoization works in Python, and the purpose of it.

Memoization acts as a cache set up for a given function with its inputs as KEY, and return values as VALUES.
Next time we send the same input, it returns from the cache rather processing.
Its an expensive technique cos it uses lot of space.

"""

from functools import lru_cache


@lru_cache(maxsize=10)
def test_memoize(n):
    total = 0
    for i in range(n):
        total+=i

    return total


import timeit

print(timeit.timeit('test_memoize(130410)', globals=globals(), number=1))
import pdb; pdb.set_trace()
print(timeit.timeit('test_memoize(2193890410)', globals=globals(), number=1))

# print(timeit.timeit('test_memoize(454322520130410)', globals=globals(), number=1))
# print(timeit.timeit('test_memoize(623523840130410)', globals=globals(), number=1))
#
#
# print(timeit.timeit('test_memoize(123213843840130410)', globals=globals(), number=1))
# print(timeit.timeit('test_memoize(454322520130410)', globals=globals(), number=1))
# print(timeit.timeit('test_memoize(623523840130410)', globals=globals(), number=1))