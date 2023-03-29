# The Liskov substitution principle: "Functions that use pointers or references to base classes must be able to use
# objects of derived classes without knowing it." See also design by contract.

class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self):
        return f'Vehicle name={self.name}'

    def get_speed(self):
        return f'Vehicle speed={self.speed}'

    def engine(self):
        # Some work
        pass

    def start_engine(self):
        self.engine()


# BAD
class Car(Vehicle):
    def start_engine(self):
        pass


# BAD
class Bicycle(Vehicle):
    def start_engine(self):
        pass


# Good, split to 2 classes with/without engine/start_engine
class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self.speed = speed

    def get_name(self):
        return f'Vehicle name={self.name}'

    def get_speed(self):
        return f'Vehicle speed={self.speed}'


class VehicleWithoutEngine(Vehicle):
    def start_engine(self):
        raise NotImplemented


class VehicleWithEngine(Vehicle):
    def engine(self):
        # Some work
        pass

    def start_engine(self):
        self.engine()


class Car(VehicleWithEngine):
    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):
    def start_moving(self):
        pass
