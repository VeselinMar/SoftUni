from unittest import TestCase, main

from Test_Trip.trip import Trip


class TestTrip(TestCase):
    DESTINATION_PRICES_PER_PERSON = {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}

    def setUp(self):
        self.trip = Trip(20_000, 2, True)
        self.small_trip = Trip(10_000, 1, False)

    def test_initialize_two_people_or_less_family_or_not_test_family_setter(self):
        self.assertEqual(self.trip.budget, 20_000)
        self.assertEqual(self.trip.travelers, 2)
        self.assertTrue(self.trip.is_family)

        self.assertEqual(self.small_trip.is_family, False)
        self.small_trip.is_family = True
        self.assertFalse(self.small_trip.is_family)

    def test_travelers_setter_zero_and_negative_number_of_travelers_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual(str(ve.exception),
                         'At least one traveler is required!')
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = -2
        self.assertEqual(str(ve.exception),
                         'At least one traveler is required!')

    def test_book_a_trip_destination_not_in_offers(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         self.trip.book_a_trip("Greece"))

    def test_book_a_trip_family_enough_budget_booked_destinations_add_budget_deduct(self):
        self.trip.book_a_trip("Australia")
        self.assertEqual(self.trip.booked_destinations_paid_amounts,
                         {"Australia": 10260.0})
        self.assertEqual(self.trip.budget,
                         9740.0)

    def test_book_a_trip_not_family_enough_budget_booked_destinations_add_budget_deduct(self):
        self.small_trip.book_a_trip("Australia")
        self.assertEqual(self.small_trip.booked_destinations_paid_amounts,
                         {"Australia": 5700})
        self.assertEqual(self.small_trip.budget,
                         4300)

    def test_book_a_trip_family_not_family_not_enough_budget_destinations_budget_check(self):
        self.trip.budget = 10_000
        self.assertEqual('Your budget is not enough!',
                         self.trip.book_a_trip("Australia"))
        self.assertEqual(self.trip.booked_destinations_paid_amounts,
                         {})
        self.assertEqual(self.trip.budget,
                         10_000)

        self.small_trip.budget = 5_000
        self.assertEqual('Your budget is not enough!',
                         self.small_trip.book_a_trip("Australia"))
        self.assertEqual(self.small_trip.booked_destinations_paid_amounts,
                         {})
        self.assertEqual(self.small_trip.budget,
                         5_000)

    def test_book_multiple_trips_family_enough_budget(self):
        t = Trip(25000.0, 2, False)

        res = t.book_a_trip('Bulgaria')
        res2 = t.book_a_trip('New Zealand')
        self.assertEqual(t.booked_destinations_paid_amounts, {'Bulgaria': 1000.0, 'New Zealand': 15000.0})
        self.assertEqual(t.budget, 9000.0)
        self.assertEqual(res, 'Successfully booked destination Bulgaria! Your budget left is 24000.00')
        self.assertEqual(res2, 'Successfully booked destination New Zealand! Your budget left is 9000.00')

    def test_booking_status_no_booked_destinations(self):
        expected_return_single_destination = ('Booked Destination: Bulgaria\n'
                                              'Paid Amount: 500.00\n'
                                              'Number of Travelers: 1\n'
                                              'Budget Left: 9500.00')
        expected_return_multiple_destinations = ("Booked Destination: Brazil\n"
                                                 "Paid Amount: 11160.00\n"
                                                 "Booked Destination: Bulgaria\n"
                                                 "Paid Amount: 900.00\n"
                                                 "Number of Travelers: 2\n"
                                                 "Budget Left: 7940.00")
        self.assertEqual(self.trip.booking_status(),
                         f'No bookings yet. Budget: {self.trip.budget:.2f}')
        self.trip.book_a_trip("Bulgaria")
        self.trip.book_a_trip("Brazil")
        self.assertEqual(self.trip.booking_status(),
                         expected_return_multiple_destinations)
        self.small_trip.book_a_trip("Bulgaria")
        self.assertEqual(self.small_trip.booking_status(),
                         expected_return_single_destination)


if __name__ == "__main__":
    main()
