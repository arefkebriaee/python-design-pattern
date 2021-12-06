'''
    Car => Benz, Bmw => suv, coupe 
        benz suv => gla, glc
        bmw suv  => x1 x3
        -----------------------
        benz coupe => cls, e-class
        bmw coupe  => z4, m1
'''

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def suv_cars(self, model):
        pass
# -------------------------------------------------

    @abstractmethod
    def coupe_cars(self, model):
        pass
# -------------------------------------------------


class Bmw(Car):
    def suv_cars(self, model):
        return model

    def coupe_cars(self, model):
        return model

# -------------------------------------------------


class Benz(Car):
    def suv_cars(self, model):
        return model

    def coupe_cars(self, model):
        return model

# -------------------------------------------------


class Suv(ABC):
    @abstractmethod
    def suv_creator(self, model):
        pass


class Coupe(ABC):
    @abstractmethod
    def coupe_creator(self, model):
        pass

# -------------------------------------------------


class Gla(Suv, Benz):
    def suv_creator(self):
        print("Your Benz suv Gla is ready.")


class Glc(Suv, Benz):
    def suv_creator(self):
        print("Your Benz suv Glc is ready")


class X1(Suv, Bmw):
    def suv_creator(self):
        print("Your Bmw suv X1 is ready.")


class X3(Suv, Bmw):
    def suv_creator(self):
        print("Your Bmw suv X3 is ready.")
# -------------------------------------------------


class Cls(Coupe, Benz):
    def coupe_creator(self):
        print("Your Benz coupe Cls is ready.")


class E_class(Coupe, Benz):
    def coupe_creator(self):
        print("Your Benz coupe E-class is ready.")


class Z4(Coupe, Bmw):
    def coupe_creator(self):
        print("Your Bmw coupe Z4 is ready.")


class M1(Coupe, Bmw):
    def coupe_creator(self):
        print("Your Bmw coupe M1 is ready.")

# -------------------------------------------------


def client_suv(brand, model):
    if issubclass(model, brand):
        your_car = brand().suv_cars(model())
        your_car.suv_creator()
    else:
        raise NameError()


def client_coupe(brand, model):
    if issubclass(model, brand):
        your_car = brand().coupe_cars(model())
        your_car.coupe_creator()
    else:
        raise NameError()


# -------------------------------------------------
try:
    client_suv(Benz, Gla)
except (NameError, AttributeError):
    print("company has not this model")

try:
    client_coupe(Bmw, Z4)
except (NameError, AttributeError):
    print("company has not this model")
