'''
    Builder design pattern
        type: creational
'''

from abc import ABC, abstractmethod

# ---------------------------------------------


class Director:
    def set_builder(self, company):
        self.builder = company

    def make_car(self):
        client_car = Car()

        client_car_body = self.builder.get_body()
        client_car.set_body(client_car_body)

        client_car_engine = self.builder.get_engine()
        client_car.set_engine(client_car_engine)

        client_car_wheel = self.builder.get_wheel()
        client_car.set_wheel(client_car_wheel)

        return client_car

# ---------------------------------------------


class Car:
    def __init__(self):
        self.__body = None
        self.__engine = None
        self.__wheel = None

    def set_body(self, body):
        self.__body = body

    def set_engine(self, engine):
        self.__engine = engine

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def detail(self):
        print("Your car detail is:")
        print(f"Body Type: {self.__body}")
        print(f"Engine Power: {self.__engine}")
        print(f"Wheel Size: {self.__wheel}")


# ---------------------------------------------

class Builder(ABC):
    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_wheel(self):
        pass

# --------------------


class Frrari(Builder):
    def get_body(self):
        body = Body()
        body.body_type = 'super sport'
        return body.body_type

    def get_engine(self):
        engine = Engine()
        engine.engine_power_hp = 950
        return engine.engine_power_hp

    def get_wheel(self):
        wheel = Wheel()
        wheel.wheel_size = 22
        return wheel.wheel_size

# --------------------


class Bmw(Builder):
    def get_body(self):
        body = Body()
        body.body_type = 'sedan'
        return body.body_type

    def get_engine(self):
        engine = Engine()
        engine.engine_power_hp = 300
        return engine.engine_power_hp

    def get_wheel(self):
        wheel = Wheel()
        wheel.wheel_size = 18
        return wheel.wheel_size

# ---------------------------------------------


class Body:
    body_type = None


class Wheel:
    wheel_size = None


class Engine:
    engine_power_hp = None
# ---------------------------------------------


company = Frrari()
my_director = Director()
my_director.set_builder(company)
my_car = my_director.make_car()
my_car.detail()
