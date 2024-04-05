from unittest import TestCase, main

from Test_Robot.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
        self.my_robot = Robot("Robi", "Military", 2, 20)

    def test_proper_initialization(self):
        bot = self.my_robot
        self.assertEqual("Robi", bot.robot_id)
        self.assertEqual("Military", bot.category)
        self.assertEqual(2, bot.available_capacity)
        self.assertEqual(20, bot.price)
        self.assertEqual([], bot.hardware_upgrades)
        self.assertEqual([], bot.software_updates)
        self.assertEqual(bot.ALLOWED_CATEGORIES, ['Military',
                                                  'Education',
                                                  'Entertainment',
                                                  'Humanoids'])
        self.assertEqual(bot.PRICE_INCREMENT, 1.5)

    def test_category_setter_not_allowed_raise(self):
        bot = self.my_robot
        bot.category = "Education"
        self.assertEqual("Education", bot.category)
        bot.category = "Entertainment"
        self.assertEqual("Entertainment", bot.category)
        bot.category = "Humanoids"
        self.assertEqual("Humanoids", bot.category)
        with self.assertRaises(ValueError) as ve:
            bot.category = "Other"
        self.assertEqual(str(ve.exception), f"Category should be one of '{self.ALLOWED_CATEGORIES}'")

    def test_price_setter_negative_raise(self):
        bot = self.my_robot
        bot.price = 1
        self.assertEqual(1, bot.price)
        bot.price = 0
        self.assertEqual(0, bot.price)
        with self.assertRaises(ValueError) as ve:
            bot.price = -1
        self.assertEqual(str(ve.exception), "Price cannot be negative!")

    def test_upgrade_already_in_upgrades_append_hardware_upgrades_increment_price_multiple_upgrades_return(self):
        bot = self.my_robot
        bot.upgrade("Processor", 40)
        self.assertEqual(f"Robot {bot.robot_id} was not upgraded.",
                         bot.upgrade("Processor", 50))
        self.assertEqual(["Processor"], bot.hardware_upgrades)
        self.assertEqual(80.0, bot.price)
        self.assertEqual(bot.upgrade("RAM", 12),
                         f'Robot {bot.robot_id} was upgraded with {"RAM"}.')
        self.assertEqual(["Processor", "RAM"], bot.hardware_upgrades)
        self.assertEqual(98.0, bot.price)

    def test_update_return_append_software_updates_reduce_capacity_multiple_older_version_error_no_capacity_error(self):
        bot = self.my_robot
        self.assertEqual(f'Robot {bot.robot_id} was updated to version {18.2}.',
                         bot.update(18.2, 1))
        self.assertEqual(bot.software_updates, [18.2])
        self.assertEqual(bot.available_capacity, 1)
        self.assertEqual(f"Robot {bot.robot_id} was not updated.",
                         bot.update(17.0, 0))
        bot.update(18.4, 0)
        self.assertEqual(f"Robot {bot.robot_id} was not updated.",
                         bot.update(18.0, 0))
        self.assertEqual(bot.software_updates, [18.2, 18.4])
        self.assertEqual(f"Robot {bot.robot_id} was not updated.",
                         bot.update(18.4, 3))
        bot.update(20.0, 1)
        self.assertEqual(bot.software_updates, [18.2, 18.4, 20.0])
        self.assertEqual(bot.available_capacity, 0)
        self.assertEqual(f"Robot {bot.robot_id} was not updated.",
                         bot.update(28.0, 3))
        self.assertEqual(bot.software_updates, [18.2, 18.4, 20.0])
        self.assertEqual(bot.available_capacity, 0)

    def test_greater_than(self):
        bot = self.my_robot
        great_bot = Robot("Brobot", "Humanoids", 90, 600)
        self.assertEqual(great_bot > bot,
                         f'Robot with ID {great_bot.robot_id} is more expensive than Robot with ID {bot.robot_id}.')
        bot.price = 600
        self.assertEqual(great_bot > bot,
                         f'Robot with ID {great_bot.robot_id} costs equal to Robot with ID {bot.robot_id}.')
        bot.price = 620
        self.assertEqual(great_bot > bot,
                         f'Robot with ID {great_bot.robot_id} is cheaper than Robot with ID {bot.robot_id}.')


if __name__ == "__main__":
    main()
