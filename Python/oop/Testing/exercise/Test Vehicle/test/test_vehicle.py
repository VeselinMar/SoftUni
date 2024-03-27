from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(60, 80)

    def test_correct_init(self):
        self.assertEqual(60, self.vehicle.fuel)
        self.assertEqual(80, self.vehicle.horse_power)
        self.assertEqual(60, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_not_enough_fuel_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_fuel_reduction(self):
        self.vehicle.drive(4)
        self.assertEqual(55, self.vehicle.fuel)

    def test_refuel_too_much_fuel_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_increase_current_fuel(self):
        self.vehicle.drive(4)
        self.vehicle.refuel(4)
        self.assertEqual(59, self.vehicle.fuel)

    def test_str_horse_power_fuel_fuel_consumption(self):
        self.assertIn(str(self.vehicle.horse_power), self.vehicle.__str__())
        self.assertIn(str(self.vehicle.fuel), self.vehicle.__str__())
        self.assertIn(str(self.vehicle.fuel_consumption), self.vehicle.__str__())


if __name__ == "__main__":
    main()
