from Python.oop.Inheritance.lab.Teacher.employee import Employee
from Python.oop.Inheritance.lab.Teacher.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return "teaching..."
