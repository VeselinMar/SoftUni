from unittest import TestCase, main

from project.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Volkswagen", "Golf", 6.7, 60)

    def test_correct_init(self):
        self.assertEqual("Volkswagen", self.car.make)
        self.assertEqual("Golf", self.car.model)
        self.assertEqual(6.7, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_invalid_make_input_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")
        with self.assertRaises(Exception) as ex:
            self.car.make = 0
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_invalid_model_input_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")
        with self.assertRaises(Exception) as ex:
            self.car.model = 0
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_invalid_fuel_consumption_invalid_input_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_invalid_fuel_capacity_invalid_input_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -6
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_invalid_fuel_amount_invalid_input_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_invalid_refuel_invalid_input_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_functionality(self):
        self.car.fuel_amount = 5
        self.car.refuel(50)
        self.assertEqual(55, self.car.fuel_amount)

    def test_refuel_fuel_over_capacity(self):
        self.car.fuel_amount = 5
        self.car.refuel(60)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_fuel_reduction(self):
        self.car.fuel_amount = 60
        self.car.drive(10)
        self.assertEqual(59.33, self.car.fuel_amount)

    def test_invalid_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")


if __name__ == "__main__":
    main()
