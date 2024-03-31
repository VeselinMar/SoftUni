from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.my_station = RailwayStation("Vienna")

    def test_initialization(self):
        self.assertEqual("Vienna", self.my_station.name)
        self.assertEqual(deque(), self.my_station.arrival_trains)
        self.assertEqual(deque(), self.my_station.departure_trains)

    def test_name_setter_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.my_station.name = "Bec"
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")
        with self.assertRaises(ValueError) as ve:
            self.my_station.name = "B"
        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrivals_on_board_append(self):
        self.my_station.new_arrival_on_board("Fast Train")
        self.assertEqual(deque(["Fast Train"]), self.my_station.arrival_trains)
        self.my_station.new_arrival_on_board("Slow Train")
        self.assertEqual(deque(["Fast Train", "Slow Train"]), self.my_station.arrival_trains)
        self.my_station.new_arrival_on_board("")
        self.assertEqual(deque(["Fast Train", "Slow Train", ""]), self.my_station.arrival_trains)

    def test_train_has_arrived_not_first_train_train_in_deque_train_missing(self):
        train = "Bullet Train"
        self.my_station.new_arrival_on_board("Fast Train")
        self.my_station.new_arrival_on_board("Slow Train")
        self.assertEqual(f"There are other trains to arrive before {train}.",
                         self.my_station.train_has_arrived(train))
        self.my_station.new_arrival_on_board(train)
        self.assertEqual(f"There are other trains to arrive before {train}.",
                         self.my_station.train_has_arrived(train))

    def test_train_has_arrived_first_train_in_deque_add_to_departures_remove_from_arrivals(self):
        train_info = "Fast Train"
        self.my_station.new_arrival_on_board(train_info)
        self.assertEqual(f"{train_info} is on the platform and will leave in 5 minutes.",
                         self.my_station.train_has_arrived(train_info))
        self.assertEqual(deque(), self.my_station.arrival_trains)
        self.assertEqual(deque([train_info]), self.my_station.departure_trains)

    def test_train_has_left_remove_from_departure_return_Bool(self):
        train_info = "Fast Train"
        self.my_station.new_arrival_on_board(train_info)
        self.my_station.train_has_arrived(train_info)
        self.assertEqual(False, self.my_station.train_has_left("Slow Train"))
        self.assertEqual(True, self.my_station.train_has_left(train_info))


if __name__ == "__main__":
    main()
