from Python.oop.Inheritance.exercise.PlayersAndMonsters.hero import Hero


class Knight(Hero):

    def __init__(self, username, level):
        super().__init__(username, level)
