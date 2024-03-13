from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck:
    @staticmethod
    def quack():
        return "Squeak"


class RobotDuck(Duck):
    MAX_HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        if self.height <= RobotDuck.MAX_HEIGHT:
            self.height += 1
        else:
            self.land()

    def land(self):
        if self.height == RobotDuck.MAX_HEIGHT:
            self.land()
        self.height = 0
