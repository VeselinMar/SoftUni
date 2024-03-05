from Wild_Cat_Zoo.caretaker import Caretaker
from Wild_Cat_Zoo.cheetah import Cheetah
from Wild_Cat_Zoo.keeper import Keeper
from Wild_Cat_Zoo.lion import Lion
from Wild_Cat_Zoo.tiger import Tiger
from Wild_Cat_Zoo.vet import Vet


class Zoo:
    # properties
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    # getters and setters
    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, new_budget):
        if isinstance(new_budget, int):
            self.__budget = new_budget

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, capacity):
        if isinstance(capacity, int):
            self.__animal_capacity = capacity

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, capacity):
        if isinstance(capacity, int):
            self.__workers_capacity = capacity

    # methods
    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum(worker.salary for worker in self.workers)
        if total_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_money_for_care = sum(animal.money_for_care for animal in self.animals)
        if sum_money_for_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion_count, tiger_count, cheetah_count = 0, 0, 0
        lion_str, tiger_str, cheetah_str = "", "", ""

        for animal in self.animals:
            if isinstance(animal, Lion):
                lion_count += 1
                lion_str += f"{animal}\n"
            elif isinstance(animal, Tiger):
                tiger_count += 1
                tiger_str += f"{animal}\n"
            elif isinstance(animal, Cheetah):
                cheetah_count += 1
                cheetah_str += f"{animal}\n"

        total_animals_count = len(self.animals)

        result = f"You have {total_animals_count} animals\n"
        result += f"----- {lion_count} Lions:\n{lion_str}" if lion_count > 0 else ""
        result += f"----- {tiger_count} Tigers:\n{tiger_str}" if tiger_count > 0 else ""
        result += f"----- {cheetah_count} Cheetahs:\n{cheetah_str}" if cheetah_count > 0 else ""

        return result.strip()

    def workers_status(self):
        keeper_count, caretaker_count, vet_count = 0, 0, 0
        keeper_str, caretaker_str, vet_str = "", "", ""

        for worker in self.workers:
            if isinstance(worker, Keeper):
                keeper_count += 1
                keeper_str += f"{worker}\n"
            elif isinstance(worker, Caretaker):
                caretaker_count += 1
                caretaker_str += f"{worker}\n"
            elif isinstance(worker, Vet):
                vet_count += 1
                vet_str += f"{worker}\n"

        total_workers_count = len(self.workers)

        result = f"You have {total_workers_count} workers\n"
        result += f"----- {keeper_count} Keepers:\n{keeper_str}" if keeper_count > 0 else ""
        result += f"----- {caretaker_count} Caretakers:\n{caretaker_str}" if caretaker_count > 0 else ""
        result += f"----- {vet_count} Vets:\n{vet_str}" if vet_count > 0 else ""

        return result.strip()


zoo = Zoo("Zootopia", 3000, 5, 8)
# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1),
           Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3),
           Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80),
           Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140),
           Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
