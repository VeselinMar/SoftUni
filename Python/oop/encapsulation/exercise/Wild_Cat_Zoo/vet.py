from Wild_Cat_Zoo.worker import Worker


class Vet(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
