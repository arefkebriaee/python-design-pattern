
class singeltone(type):
    _instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = super().__call__
        return self._instance


class person(metaclass=singeltone):
    pass


p1 = person()
p2 = person()

print(id(p1))
print(id(p2))
