import unittest

from project.worker import Worker


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 20, 100)

    def test_initialization(self):
        worker = Worker("Ivan", 20, 100)
        self.assertEqual(worker.name, "Ivan")
        self.assertEqual(worker.salary, 20)
        self.assertEqual(worker.energy, 100)

    def test_energy_incrementation_after_rest(self):
        energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy, energy + 1)

    def test_error_raised_when_working_without_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_worker_money_raised_by_salary_after_work(self):
        money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money, money + self.worker.salary)

    def test_energy_decreased_after_work(self):
        energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy, energy - 1)

    def test_get_info(self):
        result = self.worker.get_info()
        self.assertEqual(result, f'{self.worker.name} has saved {self.worker.money} money.')


if __name__ == '__main__':
    unittest.main()
