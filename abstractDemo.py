from abc import ABC, abstractmethod


class C(ABC):

    @abstractmethod
    def __init__(self):
        self.a = None
        self.b = None

    @abstractmethod
    def set_health_points(self):
        pass

    @abstractmethod
    def set_hit_points(self):
        pass


# c = C()
# print(c)

print(dir(C))