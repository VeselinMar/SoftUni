from typing import List

from Route_Management_App.route import Route
from Route_Management_App.user import User
from Route_Management_App.vehicles.cargo_van import CargoVan
from Route_Management_App.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLE_TYPES = {
        "CargoVan": CargoVan,
        "PassengerCar": PassengerCar,
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[CargoVan | PassengerCar] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point:
                if route.end_point == end_point:
                    if route.length == length:
                        return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                    elif route.length < length:
                        return f"{start_point}/{end_point} shorter route had already been added to our platform."
                    else:
                        route.is_locked = True
        route = Route(start_point, end_point, length, (len(self.routes) + 1))
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str,
                  license_plate_number: str,
                  route_id: int,
                  is_accident_happened: bool):
        driver = next((d for d in self.users if d.driving_license_number == driving_license_number), None)
        if driver.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        route = next((r for r in self.routes if r.route_id == route_id), None)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            driver.decrease_rating()
        else:
            driver.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))
        count_of_repaired_vehicles = 0
        for vehicle in sorted_vehicles[:count]:
            vehicle.change_status()
            count_of_repaired_vehicles += 1
        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: u.rating, reverse=True)
        return_string = '*** E-Drive-Rent ***\n'
        return_string += '\n'.join(str(user) for user in sorted_users)

        return return_string



