from Python.oop.Inheritance.exercise.PlayersAndMonsters.hero import Hero


class Wizard(Hero):

    def __init__(self, username, level):
        super().__init__(username, level)
