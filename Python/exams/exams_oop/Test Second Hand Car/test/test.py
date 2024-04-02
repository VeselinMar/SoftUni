from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("VW", "Golf", 250_000, 2500)

    def test_class_initialization(self):
        self.assertEqual(self.car.model, "VW")
        self.assertEqual(self.car.car_type, "Golf")
        self.assertEqual(self.car.mileage, 250_000)
        self.assertEqual(self.car.price, 2500)
        self.assertEqual(self.car.repairs, [])

    def test_price_setter_less_or_equal_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0
        self.assertEqual(str(ve.exception),
                         'Price should be greater than 1.0!')
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5
        self.assertEqual(str(ve.exception),
                         'Price should be greater than 1.0!')
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.0
        self.assertEqual(str(ve.exception),
                         'Price should be greater than 1.0!')
        with self.assertRaises(ValueError) as ve:
            self.car.price = -2
        self.assertEqual(str(ve.exception),
                         'Price should be greater than 1.0!')

    def test_mileage_setter_less_or_equal_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 1.0
        self.assertEqual(str(ve.exception),
                         'Please, second-hand cars only! Mileage must be greater than 100!')
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual(str(ve.exception),
                         'Please, second-hand cars only! Mileage must be greater than 100!')
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 0.0
        self.assertEqual(str(ve.exception),
                         'Please, second-hand cars only! Mileage must be greater than 100!')
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = -2
        self.assertEqual(str(ve.exception),
                         'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price_greater_or_equal_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2500)
        self.assertEqual(str(ve.exception),
                         'You are supposed to decrease the price!')
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2600)
        self.assertEqual(str(ve.exception),
                         'You are supposed to decrease the price!')

    def test_set_promotional_price_price_update_return_string(self):
        self.assertEqual(self.car.set_promotional_price(2000),
                         'The promotional price has been successfully set.')
        self.assertEqual(2000, self.car.price)

    def test_need_repair_impossible_repair(self):
        self.assertEqual(self.car.need_repair(1500,
                                              "Transmission"),
                         'Repair is impossible!')
        self.assertEqual(self.car.price, 2500)
        self.assertEqual(self.car.repairs, [])

    def test_need_repair_price_incrementation_append_multiple_repairs_return_string(self):
        self.assertEqual(self.car.need_repair(500,
                                              "Windshield"),
                         f'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 3000)
        self.assertEqual(self.car.repairs, ["Windshield"])
        # second repair
        self.assertEqual(self.car.need_repair(400,
                                              "New Paint"),
                         f'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 3400)
        self.assertEqual(self.car.repairs, ["Windshield", "New Paint"])

    def test_greater_than_cannot_compare(self):
        second_car = SecondHandCar("VW", "Sharan", 400_000, 4000)
        test_greater = second_car > self.car
        self.assertEqual(test_greater, 'Cars cannot be compared. Type mismatch!')

        test_greater = self.car > second_car
        self.assertEqual(test_greater, 'Cars cannot be compared. Type mismatch!')

    def test_greater_than_return_bool(self):
        second_car = SecondHandCar("VW", "Golf", 400_000, 4000)
        test_greater = second_car > self.car
        self.assertEqual(test_greater, True)

        test_greater = self.car > second_car
        self.assertEqual(test_greater, False)

    def test_string_representation(self):
        expected_return_string = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""
        self.assertEqual(str(self.car),
                         expected_return_string)


if __name__ == "__main__":
    main()
