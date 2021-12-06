'''
    Car => Benz, Bmw => suv, coupe 
        benz suv => gla
        bmw suv  => x1
        -----------------------
        benz coupe => cls
        bmw coupe  => z4
'''

from abc import ABC, abstractmethod
import abc

# ---------------------------------------


class Car(ABC):
    @abstractmethod
    def creator_suv(self):
        pass

    @abstractmethod
    def creator_coupe(self):
        pass

# -------------------


class Benz(Car):
    def creator_suv(self):
        return Gla()

    def creator_coupe(self):
        return Cls()

# -------------------


class Bmw(Car):
    def creator_suv(self):
        return X1()

    def creator_coupe(self):
        return Z4()

# ---------------------------------------


class Suv(ABC):
    @abstractmethod
    def creating_suv(self):
        pass


class Coupe(ABC):
    @abstractmethod
    def creating_coupe(self):
        pass
# ---------------------------------------


class Gla(Suv):
    def creatin_suv(self):
        print("Your suv benz gla is ready.")


class Cls(Coupe):
    def creating_coupe(self):
        print("Your coupe benz cls is ready.")


class X1(Suv):
    def creating_suv(self):
        print("Your suv bmw x1 is ready.")


class Z4(Coupe):
    def creating_coupe(self):
        print("Your coupe bmw z4 is ready.")

# ---------------------------------------


def suv(method):
    your_car = method.creator_suv()
    your_car.creator_suv()


def coupe(method):
    your_car = method.creator_coupe()
    your_car.creating_coupe()

# ---------------------------------------


coupe(Bmw())
