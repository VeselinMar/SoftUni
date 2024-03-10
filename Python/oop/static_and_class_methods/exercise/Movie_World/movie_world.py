from typing import List

from Movie_World.customer import Customer
from Movie_World.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        ordered_dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)
        client = next((customer for customer in self.customers if customer.id == customer_id), None)

        if ordered_dvd in client.rented_dvds:
            return f"{client.name} has already rented {ordered_dvd.name}"

        if ordered_dvd.is_rented:
            return "DVD is already rented"

        if ordered_dvd.age_restriction > client.age:
            return f"{client.name} should be at least {ordered_dvd.age_restriction} to rent this movie"

        client.rented_dvds.append(ordered_dvd)
        ordered_dvd.is_rented = True
        return f"{client.name} has successfully rented {ordered_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        ordered_dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)
        client = next((customer for customer in self.customers if customer.id == customer_id), None)

        try:
            client.rented_dvds.remove(ordered_dvd)
            ordered_dvd.is_rented = False
            return f"{client.name} has successfully returned {ordered_dvd.name}"
        except ValueError:
            return f"{client.name} does not have that DVD"

    def __repr__(self):
        customers = '\n'.join([customer.__repr__() for customer in self.customers])
        dvds = '\n'.join([dvd.__repr__() for dvd in self.dvds])

        return f"{customers}\n{dvds}"


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
