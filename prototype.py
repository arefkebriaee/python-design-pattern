'''
    Prototype design pattern
        type: creational
            make a copy from an object
'''

from copy import deepcopy


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Prototype:
    def __init__(self):
        self._object = {}

    def register(self, name, obj):
        self._object[name] = obj

    def unregister(self, name):
        del self._object[name]

    def clone(self, name, **kwargs):
        cloned_obj = deepcopy(self._object.get(name))
        cloned_obj.__dict__.update(kwargs)
        return cloned_obj

# -------------------------------------------------------------


p1 = Person('alex', 38, 'male')

prop1 = Prototype()
prop1.register('person-1', p1)
person_copy = prop1.clone('person-1')

print(p1.__dict__)
print(person_copy.__dict__)
# --------------
print(id(p1.name))
print(id(person_copy.name))
# --------------
person_copy = prop1.clone('person-1', age=40)
print(p1.__dict__)
print(person_copy.__dict__)
