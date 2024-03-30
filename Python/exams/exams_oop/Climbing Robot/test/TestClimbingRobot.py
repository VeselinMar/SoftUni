from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot("Alpine", "BMW", 100, 100)

    def test_correct_init(self):
        self.assertEqual("Alpine", self.robot.category)
        self.assertEqual("BMW", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_incorrect_category_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Milano"

        self.assertEqual(f"Category should be one of {self.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity_empty_and_filled(self):
        software = {'name': 'Win95',
                    'capacity_consumption': 20,
                    'memory_consumption': 30,
                    }
        self.assertEqual(0, self.robot.get_used_capacity())
        self.robot.install_software(software)
        self.assertEqual(20, self.robot.get_used_capacity())

    def test_get_available_capacity_empty_and_filled(self):
        software = {'name': 'Win95',
                    'capacity_consumption': 20,
                    'memory_consumption': 30,
                    }
        self.assertEqual(100, self.robot.get_available_capacity())
        self.robot.install_software(software)
        self.assertEqual(80, self.robot.get_available_capacity())

    def test_get_used_memory_empty_and_filled(self):
        software = {'name': 'Win95',
                    'capacity_consumption': 20,
                    'memory_consumption': 30,
                    }
        self.assertEqual(0, self.robot.get_used_memory())
        self.robot.install_software(software)
        self.assertEqual(30, self.robot.get_used_memory())

    def test_get_available_memory_empty_and_filled(self):
        software = {'name': 'Win95',
                    'capacity_consumption': 20,
                    'memory_consumption': 30,
                    }
        self.assertEqual(100, self.robot.get_available_memory())
        self.robot.install_software(software)
        self.assertEqual(70, self.robot.get_available_memory())

    def test_install_software_add_to_installed_software(self):
        software = {'name': 'Win95',
                    'capacity_consumption': 20,
                    'memory_consumption': 30,
                    }
        additional_software = {'name': 'WinXP',
                               'capacity_consumption': 70,
                               'memory_consumption': 60,
                               }

        self.robot.install_software(software)
        self.assertEqual([software], self.robot.installed_software)
        self.robot.install_software(additional_software)
        self.assertEqual([software, additional_software], self.robot.installed_software)

    def test_install_software_check_return_statement_check_fill_memory_and_capacity_check_cannot_be_installed(self):
        software = {'name': 'Win95',
                    'capacity_consumption': 20,
                    'memory_consumption': 30,
                    }

        second_software = {'name': 'Windows10',
                           'capacity_consumption': 80,
                           'memory_consumption': 70,
                           }

        additional_software = {'name': 'WinXP',
                               'capacity_consumption': 90,
                               'memory_consumption': 60,
                               }

        self.assertEqual(self.robot.install_software(software),
                         f"Software '{software['name']}'"
                         f" successfully installed on {self.robot.category} part.")
        self.assertEqual(self.robot.install_software(second_software),
                         f"Software '{second_software['name']}'"
                         f" successfully installed on {self.robot.category} part.")
        self.assertEqual(self.robot.install_software(additional_software),
                         f"Software '{additional_software['name']}'"
                         f" cannot be installed on {self.robot.category} part.")

    def test_install_software_fail_memory_condition(self):
        software = {'name': 'Win95',
                    'capacity_consumption': 20,
                    'memory_consumption': 30,
                    }

        second_software = {'name': 'Windows10',
                           'capacity_consumption': 80,
                           'memory_consumption': 75,
                           }

        self.robot.install_software(software)
        self.assertEqual(self.robot.install_software(second_software),
                         f"Software '{second_software['name']}'"
                         f" cannot be installed on {self.robot.category} part.")

    def test_install_software_fail_capacity_condition(self):
        software = {'name': 'Win95',
                    'capacity_consumption': 20,
                    'memory_consumption': 30,
                    }

        second_software = {'name': 'Windows10',
                           'capacity_consumption': 85,
                           'memory_consumption': 70,
                           }

        self.robot.install_software(software)
        self.assertEqual(self.robot.install_software(second_software),
                         f"Software '{second_software['name']}'"
                         f" cannot be installed on {self.robot.category} part.")


if __name__ == "__main__":
    main()
