from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Robert", "Cat", "Meow")

    def test_correct_init(self):
        self.assertEqual("Robert", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        # kingdom check?

    def test_make_sound_name_sound(self):
        name, sound = self.mammal.make_sound().split(" makes ")
        self.assertEqual("Robert", name)
        self.assertEqual("Meow", sound)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_name_type(self):
        name, type = self.mammal.info().split(" is of type ")
        self.assertEqual("Robert", name)
        self.assertEqual("Cat", type)


if __name__ == "__main__":
    main()
