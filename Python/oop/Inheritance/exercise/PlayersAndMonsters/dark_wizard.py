from Python.oop.Inheritance.exercise.PlayersAndMonsters.wizard import Wizard


class DarkWizard(Wizard):

    def __init__(self, username, level):
        super().__init__(username, level)
