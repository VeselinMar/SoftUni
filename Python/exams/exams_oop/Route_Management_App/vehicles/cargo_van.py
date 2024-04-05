from Route_Management_App.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00
    EXTRA_PERCENTAGE_LOSS = 5

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage_of_max_mileage = (mileage / self.MAX_MILEAGE) * 100 + self.EXTRA_PERCENTAGE_LOSS

        battery_reduction_percentage = round(percentage_of_max_mileage)
        self.battery_level -= battery_reduction_percentage
